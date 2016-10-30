'''
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

# To be implemented soon
#include <stdio.h>
#include <vector>
#include <limits.h>
#include <algorithm>
using namespace std;
int print(vector<int> A, int B) {
	int i,j,k,sum=INT_MAX,ans, temp;
	int n = A.size();
	sort(A.begin(), A.end());
	for(i=0;i<n;i++) {
		k=n-1;
		j=i+1;
		temp = B-A[i];
		while(j<k) {
			if(abs(A[i]+A[j]+A[k]-B)<sum) {
				sum = abs(A[i]+A[j]+A[k]-B);
				ans = A[i]+A[j]+A[k];
			}
			if(A[j]+A[k] < temp) {
				j++;	
			}
			else {
				k--;
			}
			
		}
	}
	return ans;
}
int main() {
	printf("Hello world\n");
	vector<int> v;
	v.push_back(5);
	v.push_back(-2);
	v.push_back(-1);
	v.push_back(-10);
	v.push_back(10);


	printf("%d\n",print(v,5));
}
