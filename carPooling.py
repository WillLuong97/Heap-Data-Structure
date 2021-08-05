#1094. Car Pooling


'''
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 



Approach: sort the array trips by the distance of the starting locations from smallest to largest, then from there we will create a priority queue to process the current trip

For the processing, we will peek at the element at the head of the list and see if the trip has reached its destination by the time we start our next trip or not

if it is not yet reached its destination, we will decrement the capacity by the number of passenger of the next trip and add the the second trip onto the queue

'''
import heapq
def carPooling(trips, capacity):
	#base case: the trips is empty and the capacity is 0
	if(not trips or trips == [[]]):
		return True

	if(len(trips) == 1):
		if trips[0][0] <= capacity:
			return True
		return False

	#sort the trip by the starting locations from the smallest to highest 
	trips.sort(key=lambda x:x[1])
	#create a heap to keep track of each nodes
	h= []
	#looping through each trips in the array  
	for passenger, start, end in trips:
		while h and h[0][0] <= start: 
			capacity += trips[1][0]
			heapq.heappop(h)
		#if the heap was empty, meaning the car was empty, we will add the passenger onto it and start the trip
		if not h:
			if capacity >= passenger: 
				heapq.heappush(h, (end, (passenger, start, end)))
				capacity -= passenger
		#If we still have spots, then keep adding the passenger onot the seat
		elif capacity >= passenger:
			heappush(h, (end, (passenger, start, end)))
			capacity -= passenger
		else:
			return False
	return True


			
	
	

#Main function to run the program  
def main():
	print("TESTING 1094. Car Pooling...")
	
	trips = [[2,1,5],[3,3,7]]
	capacity = 4
	print(carPooling(trips, capacity))

		

	print("END OF TESTING...")


main()
