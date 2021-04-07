#Problem 355. Design Twitter
'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

Observation: 
- Followee cannot see the follower's twitters, if they didn't follow them on their newsfeed
- Follower can see their own tweets and the tweets of people they followed. 
- Follower cannot see the tweets of people that their followee followed. 
- Every tweets are unique to themselves.
Requirements: 
- We need a data structure that can: 
	+ Keep track of the tweets that each user can see, i.e, their own tweets and followee's tweets
	+ Make sure that the tweets of people that they  did not follow cannont be seen by them 
	+ Keep track of the tweets owner, example:  user 1 created and posted tweet 2; user 2 created and posted tweet 3
'''
class Twitter(object):
	#constructor: 
	def __init__(self):
		#Hash map to store the user/user_tweets and followers/followeeID:
		self.userWithTweets = {}
		self.followersWithFollowee = {}
		#a variable to keep track of the time the tweet is created
		self.assign_priority = 0
	#Function to post tweet: 
	'''
		Compose a new tweet.
		:type userId: int
		:type tweetId: int
		:rtype: None
	'''
	def postTweet(self, userId, tweetId):
		self.assign_priority += 1
		#Adding the userID and the tweetID into the dictionary
		#if the user has created a tweet before then we will just keep appending new tweets into the dictionary
		if userId in self.userWithTweets:
			self.userWithTweets[userId].add((tweetId, self.assign_priority))
		else: 
			self.userWithTweets[userId] = set([(tweetId, self.assign_priority)])
		return self.userWithTweets
	#Function to get news feed: 
	'''
		Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
		:type userId: int
		:rtype: List[int]
	'''	
	def getNewsFeed(self, userId):
		#array to store the value of all followees that the user follows
		arrayOfUserIds = [userId]
		result = []
		if userId in self.followersWithFollowee:
			for followee in self.followersWithFollowee[userId]:
				arrayOfUserIds.append(followee)
		#helper method to get all tweets belong those user ids
		def getTweetIds(array):
			retArr = []
			for user in array:
				if user in self.userWithTweets:
					for tweet in self.userWithTweets[user]:
						retArr.append(tweet)
			return retArr
		tweets = getTweetIds(arrayOfUserIds)
		while len(tweets) > 10:
			tweets.pop()

		tweets = sorted(tweets, key=lambda posts: posts[1], reverse=True)
		for tweet in tweets:
			result.append(tweet[0])
		return result

	#Function to follow a user: 
	'''
		Follower follows a followee. If the operation is invalid, it should be a no-op.
		:type followerId: int
		:type followeeId: int
		:rtype: None

	'''	
	def follow(self, followerId, followeeId):
		#adding the followerid and followeeId relationship into the hash map
		if followerId in self.followersWithFollowee:
			self.followersWithFollowee[followerId].add(followeeId)
		else: 
			self.followersWithFollowee[followerId] = set([followeeId])
		return self.followersWithFollowee
	#Function to unfollow a user:
	"""
	Follower unfollows a followee. If the operation is invalid, it should be a no-op.
	:type followerId: int
	:type followeeId: int
	:rtype: None
	"""
	def unfollow(self, followerId, followeeId): 
		#find the follower and look through the followeeId and remove the unfollowed user
		if followerId in self.followersWithFollowee:
			if followeeId in self.followersWithFollowee[followerId]:
				self.followersWithFollowee[followerId].remove(followeeId)
		
		return self.followersWithFollowee		
#Main function to run the test cases:
def main():
	print("Testing DESIGN TWITTER...")

#	#Testing component: 
	obj = Twitter()
	obj.postTweet(1,5)
	obj.postTweet(1,2)
	obj.postTweet(3, 10)
	
	param_2 = obj.getNewsFeed(1)
	print(param_2)
	obj.follow(1,3)
	param_2 = obj.getNewsFeed(1)

	print(param_2)

	#print(obj.follow(3, 6))
	#print(obj.unfollow(1, 3))

	print("END OF TESTING...")

main()
