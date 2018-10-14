from linear_algebra import squared_distance, vector_mean, distance 
import math, random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 

class kMeans:
	#perfomrs k-means clustering
	def __init__(self, k):
		self.k = k 					#number of cluster
		self.means = None
		self.assignments_cluster = None	#test to plot image


	def classify(self, input):
		#return the index of the cluster closest to the input
		return min(range(self.k), key=lambda i: squared_distance(input, self.means[i]))


	def train(self, input):
		#choose k random points as the initial means
		self.means = random.sample(inputs, self.k)
		assignments = None

		while True:
			#find new assigments
			new_assignments = list(map(self.classify, inputs))
			print(new_assignments)
			#if not assignments have change, we're done
			if assignments == new_assignments:
				return

			#otherwise keep the new assignments
			assignments = new_assignments

			#only to plot image
			self.assignments_cluster = new_assignments

			#and compute new means based on the new assignments
			for i in range(self.k):
				#find all points assignments to cluster i
				i_points = [p for p, a in zip(inputs, assignments) if a==i]

				#make sure i_points is not empty so don't divide by 0
				if i_points:
					self.means[i] = vector_mean(i_points)


inputs = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]
assignments_cluster = None

random.seed(4)
clusterer = kMeans(3)
clusterer.train(inputs)
print(clusterer.means)


print("new assignments...")
print(clusterer.assignments_cluster)


for i in range(len(clusterer.assignments_cluster)):
	if clusterer.assignments_cluster[i] ==2 :
		plt.scatter(inputs[i][0],inputs[i][1], color='black')



x = [a[0] for a in inputs]
y = [b[1] for b in inputs]


for i in range(len(clusterer.means)):
	plt.scatter(clusterer.means[i][0], clusterer.means[i][1],color='blue')

#plt.scatter(x, y, c='black',s=7)
plt.show()
#plt.inshow(new_img)