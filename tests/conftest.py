import pytest
from application import create_app, db
# Examples of imports:
# import pytest
# from application import create_app, db
# from application.models import User, Post

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # # Insert user data
    # user1 = User(email='patkennedy79@gmail.com',
    #              password_plaintext='FlaskIsAwesome')
    # user2 = User(email='kennedyfamilyrecipes@gmail.com',
    #              password_plaintext='PaSsWoRd')
    #
    # post1 = Post('Post Title', 'Post Content',
    #              'https://github.com/', 'https://image.com/', False, slug='post-title')
    # post2 = Post('Post Title2', 'Post Content2',
    #              'https://github2.com/', 'https://image2.com/', False, slug='post-title2')
    #
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.add(post1)
    # db.session.add(post2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()








#Example of fixtures:

# @pytest.fixture(scope='module')
# def new_user():
#     user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
#     return user
#
#
# @pytest.fixture(scope='module')
# def new_post():
#     post = Post('Post Title', 'Post Content',
#                 'https://github.com/', 'https://image.com/', False, slug='post-title')
#     return post

# @pytest.fixture(scope='function')
# def login_default_user(test_client):
#     test_client.post('/login',
#                      data=dict(email='patkennedy79@gmail.com',
#                                password='FlaskIsAwesome'),
#                      follow_redirects=True)
#
#     yield  # this is where the testing happens!
#
#     test_client.get('/logout', follow_redirects=True)