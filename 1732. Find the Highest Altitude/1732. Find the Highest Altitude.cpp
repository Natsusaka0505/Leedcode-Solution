#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int largestAltitude(vector<int> &gain)
{
  int n = gain.size();
  vector<int> res(n + 1);

  res[0] = 0; // Initialize the first element directly

  for (int i = 0; i < n; i++)
  {
    res[i + 1] = res[i] + gain[i]; // Use i + 1 to access the correct index in res
  }

  return *max_element(res.begin(), res.end());
}

int main(void)
{
  vector<int> gain = {-5, 1, 5, 0, -7};

  cout << largestAltitude(gain);
}
