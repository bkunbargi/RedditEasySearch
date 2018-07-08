from distutils.core import setup

setup(name='RedditEasySearch',
      version='0.1',
      description='Search by subreddits and topics',
      author='Bisher Kunbargi',
      author_email='b.kunbargi@gmail.com',
      packages=['RedditEasySearch'],
      install_requires = ['praw']
     )
