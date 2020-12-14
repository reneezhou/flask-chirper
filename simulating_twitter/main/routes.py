from secrets import randbits
from flask import render_template, redirect, url_for
from flask.blueprints import Blueprint
from flask_login import current_user, login_required
from simulating_twitter import db
from simulating_twitter.models import Post
from simulating_twitter.post.utils import show_time
from simulating_twitter.post.forms import PostForm


main = Blueprint('main', __name__)

@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(post_id = randbits(60), content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))

    posts = Post.query.order_by(Post.date_posted.desc()).all()
    for post in posts:
        post.show = show_time(post.date_posted)
    # .profile_image is a column from the User model 
    return render_template('home.html', form = form, posts = posts)


@main.route('/explore', methods = ['GET', 'POST'])
def explore():
    return render_template('explore.html', trends = trends, happenings = happenings)


@main.route('/notifications')
@login_required
def notifications():
    return render_template('notifications.html')


@main.route('/notifications/mentions')
@login_required
def notifications_mentions():
    return render_template('notifications_mentions.html')


@main.route('/messages')
@login_required
def messages():
    return render_template('messages.html')


@main.route('/follower_requests')
def followerRequests():
    return render_template('followerRequests.html')


# i
@main.route('/bookmarks')
@login_required
def bookmarks():
    return render_template('bookmarks.html')


# i
@main.route('/lists/create')
@login_required
def lists_create():
    return render_template('lists_create.html')


# i
@main.route('/lists/add_member')
@login_required
def lists_addMember():
    return render_template('lists_addMember.html')


# i
@main.route('/trends')
@login_required
def trends():
    return render_template('trends.html', trends = trends)


# i
@main.route('/timeline')
@login_required
def timeline():
    return render_template('timeline.html', happenings = happenings)


# i
@main.route('/connect_people')
@login_required
def connect_people():
    return render_template('connect_people.html')


# i
@main.route('/display')
def display():
    return render_template('display.html')


# i
@main.route('/keyboard_shortcuts')
def keyboardShortcuts():
    return render_template('keyboardShortcuts.html')





# posts = [
#     {
#         'icon': 'icon 1',
#         'username': 'username 1',
#         'handle': '@handle 1',
#         'time': 'date 1',
#         'content': 'content 1',
#         'comment': 'comment button 1',
#         'rechirp': 'rechirp button 1',
#         'like': 'like button 1',
#         'share': 'share buttton dropdown 1'
#     },
#     {
#         'icon': 'icon 2',
#         'username': 'username 2',
#         'handle': '@handle 2',
#         'time': 'date 2',
#         'content': 'content 2',
#         'comment': 'comment button 2',
#         'rechirp': 'rechirp button 2',
#         'like': 'like button 2',
#         'share': 'share buttton dropdown 2'
#     },
# ]

trends = [
    {
        'label': 'label 1',
        'topic': 'topic 1',
        'content': 'content 1',
        'chirp_count': 'count 1'
    },
    {
        'label': 'label 2',
        'topic': 'topic 2',
        'content': 'content 2',
        'chirp_count': 'count 2'
    }
]

happenings = [
    {
        'label': 'label 1',
        'time': 'time 1',
        'title': 'title 1'
    },
    {
        'label': 'label 2',
        'time': 'time 2',
        'title': 'title 2'
    }
]

people = [
    {   
        'icon': 'icon 1',
        'username': 'username 1',
        'handle': '@handle 1'
    },
    {
        'icon': 'icon 2',
        'username': 'username 2',
        'handle': '@handle 2'
    }
]