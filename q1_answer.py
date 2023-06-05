# Principles of Algorithm Design
#
# Final Exam, Question 1
#
# Student Name: Hamed Araab
# Student Number: 9925003


from math import log
from random import sample


class KMeansClustering:
    """
    Performs the k-means clustering algorithm on a list of points with the
    specified number of clusters (`k`).

    ### Notes:

    - The algorithm will be performed `max(100, int(math.log(len(points))))`
    times and the result with the lowest Within-Cluster Sum of Squares (`WCSS`)
    is selected as the final output.

    - If any cluster becomes empty at any point, that iteration of performing
    the k-means algorithm will be aborted.
    """

    @staticmethod
    def _get_distance(point1, point2):
        """
        Returns the Euclidean distance between two points.
        """

        if len(point1) != len(point2):
            raise ValueError("Both points must have the same number of dimensions.")

        return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

    def __init__(self, points, k):
        self._points = points
        self._k = k

        self._run()

    @property
    def points(self):
        return self._points

    @property
    def k(self):
        return self._k

    @property
    def means(self):
        return self._means

    @property
    def clusters(self):
        return self._clusters

    @property
    def min_inter_cluster_distance(self):
        """
        The shortest distance inter-cluster distance.
        """

        min_distance = float("inf")

        for i in range(self._k):
            for j in range(i + 1, self._k):
                for point_i in self._clusters[i]:
                    for point_j in self._clusters[j]:
                        distance = KMeansClustering._get_distance(point_i, point_j)
                        min_distance = min(distance, min_distance)

        return min_distance

    def _get_initial_means(self):
        """
        Returns `k` random points as the initial values for means.
        """

        return sample(self._points, k=self._k)

    def _get_clusters(self):
        """
        Returns a list of clusters with each containing at least one point.
        """

        clusters = [[] for _ in range(self._k)]

        for point in self._points:
            distances = [
                KMeansClustering._get_distance(point, mean) for mean in self._means
            ]

            nearest_mean_index = distances.index(min(distances))

            clusters[nearest_mean_index].append(point)

        return clusters

    def _get_means(self):
        """
        Returns the means of all clusters.
        """

        return [
            [sum(coords) / len(cluster) for coords in zip(*cluster)]
            for cluster in self._clusters
        ]

    def _get_wcss(self):
        """
        Returns the Within-Cluster Sum of Squares (`WCSS`) metric for the current
        clustering result.
        """

        return sum(
            (x - y) ** 2
            for cluster, mean in zip(self._clusters, self._means)
            for point in cluster
            for x, y in zip(point, mean)
        )

    def _run(self):
        """
        Finds the best clustering result for this instance.
        """

        iterations = max(100, int(log(len(self._points))))

        # Keeps a dictionary of WCSS's and clustering results as keys and
        # values.
        history = {}

        for _ in range(iterations):
            self._prev_means = None
            self._means = self._get_initial_means()

            try:
                while self._means != self._prev_means:
                    self._clusters = self._get_clusters()

                    self._prev_means = self._means
                    self._means = self._get_means()

                wcss = self._get_wcss()
                history[wcss] = self._clusters
            except ZeroDivisionError:
                continue

        # Assign the clustering result with the lowest WCSS to the final
        # clustering result.
        self._clusters = history[min(history.keys())]
        self._means = self._get_means()


def main():
    # Start of getting user inputs

    points_count = int(input())
    points = [list(map(float, input().split(" "))) for _ in range(points_count)]
    clusters_count = int(input())

    # End of getting user inputs

    clustering = KMeansClustering(points, clusters_count)

    print("{:.7f}".format(clustering.min_inter_cluster_distance))


if __name__ == "__main__":
    main()
