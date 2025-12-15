from datetime import datetime, timedelta

import pytest
import pytz
from django.contrib.auth import get_user_model
from io import BytesIO
from PIL import Image
from django.core.files.images import ImageFile
from conftest import N_PER_PAGE

N_TEST_POSTS = 4
N_POSTS_LIMIT = 5


@pytest.fixture
def posts():
    # If project provides a `posts` list in blog.views, use it so both
    # the fixture and the project share identical data.
    try:
        from blog.views import posts as project_posts
    except Exception:
        project_posts = None

    if isinstance(project_posts, list):
        return project_posts

    import datetime as _dt
    # Fallback: provide a simple list of post-like dicts for template-only tests
    return [
        {
            'id': i,
            'title': f'Title {i}',
            'text': f'Post text {i} ' + ('x' * 40),
            'pub_date': _dt.datetime.now(),
            'location': {'name': 'Планета Земля', 'is_published': True},
            'author': {'username': f'user{i}'},
            'category': {'title': 'category_slug', 'slug': 'category_slug', 'is_published': True}
        }
        for i in range(N_TEST_POSTS)
    ]


@pytest.fixture
def published_locations(mixer):
    return mixer.cycle(N_TEST_POSTS).blend('blog.Location')


@pytest.fixture
def unpublished_locations(mixer):
    return mixer.cycle(N_TEST_POSTS).blend('blog.Location', is_published=False)


@pytest.fixture
def posts_with_unpublished_category(mixer, user):
    return mixer.cycle(N_TEST_POSTS).blend(
        'blog.Post', author=user, category__is_published=False)


@pytest.fixture
def posts_with_future_date(mixer, user):
    date_later_now = (
        datetime.now(tz=pytz.UTC) + timedelta(days=date)
        for date in range(1, 11)
    )
    return mixer.cycle(N_TEST_POSTS).blend(
        'blog.Post', author=user, pub_date=date_later_now)


@pytest.fixture
def posts_with_published_locations(
    mixer, user, published_locations, published_category):
    return mixer.cycle(N_TEST_POSTS).blend(
        'blog.Post', author=user, category=published_category,
        location=mixer.sequence(*published_locations))


@pytest.fixture
def unpublished_posts_with_published_locations(
        mixer, user, published_locations, published_category):
    return mixer.cycle(N_TEST_POSTS).blend(
        'blog.Post', author=user, is_published=False, category=published_category,
        location=mixer.sequence(*published_locations))


@pytest.fixture
def posts_with_published_locations_from_another_published_category(
        mixer, user, published_locations, another_published_category):
    return mixer.cycle(N_TEST_POSTS).blend(
        'blog.Post', author=user, category=another_published_category,
        location=mixer.sequence(*published_locations))


@pytest.fixture
def posts_with_unpublished_locations(
        mixer, user, published_category, unpublished_locations):
    return mixer.cycle(N_TEST_POSTS).blend(
        'blog.Post', author=user, location=mixer.sequence(*unpublished_locations),
        category=published_category)


@pytest.fixture
def published_category(mixer):
    return mixer.blend('blog.Category', is_published=True)


@pytest.fixture
def another_published_category(mixer):
    return mixer.blend('blog.Category', is_published=True)


@pytest.fixture
def published_location(mixer):
    return mixer.blend('blog.Location', is_published=True)


@pytest.fixture
def unpublished_location(mixer):
    return mixer.blend('blog.Location', is_published=False)


@pytest.fixture
def unpublished_post(mixer, user):
    return mixer.blend('blog.Post', author=user, is_published=False)


@pytest.fixture
def unpublished_category(mixer):
    return mixer.blend('blog.Category', is_published=False)


@pytest.fixture
def post_with_unpublished_category(mixer, user, unpublished_category):
    return mixer.blend('blog.Post', author=user, category=unpublished_category)


@pytest.fixture
def post_with_published_location(
        mixer, user, published_location, published_category):
    img = Image.new('RGB', (100, 100), color=(73, 109, 137))
    img_io = BytesIO()
    img.save(img_io, format='JPEG')
    img_io.seek(0)
    image_file = ImageFile(img_io, name='temp_image.jpg')
    post = mixer.blend('blog.Post', author=user, location=published_location,
                       category=published_category)
    # Save the in-memory image into the model ImageField so .url is available
    post.image.save('temp_image.jpg', image_file, save=True)
    return post


@pytest.fixture
def post_with_unpublished_location(
        mixer, user, unpublished_location, published_category):
    return mixer.blend(
        'blog.Post', author=user, category=published_category,
        location=unpublished_location)


@pytest.fixture
def post_with_future_date(mixer, user):
    date_later_now = datetime.now(tz=pytz.UTC) + timedelta(days=1)
    return mixer.blend('blog.Post', author=user, pub_date=date_later_now)


@pytest.fixture
def author(mixer):
    User = get_user_model()
    return mixer.blend(User)


@pytest.fixture
def many_posts_with_published_locations(
        mixer, user, published_locations, published_category):
    return mixer.cycle(N_PER_PAGE * 2).blend(
        'blog.Post', author=user, category=published_category,
        location=mixer.sequence(*published_locations))


@pytest.fixture
def posts_with_author(mixer, author):
    return mixer.cycle(2).blend('blog.Post', author=author)
