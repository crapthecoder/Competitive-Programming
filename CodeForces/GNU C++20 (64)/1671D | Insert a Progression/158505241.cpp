bits/stdc++.h>
namespace std;

endl '\n'
int long long

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n, x; cin >> n >> x;

int a[n];
for (int i = 0; i < n; i++)
cin >> a[i];

int mini = *min_element(a, a+n), maxi = *max_element(a, a+n);

int total = 0;
for (int i = 1; i < n; i++)
total += abs(a[i] - a[i-1]);

(mini > 1) {
int cur = min(a[0] - 1, a[n-1] - 1);
for (int i = 0; i < n-1; i++)
cur = min(cur, a[i] + a[i+1] - 2 - abs(a[i] - a[i+1]));

total += cur;


(maxi < x) {
int cur = min(x - a[0], x - a[n-1]);
for (int i = 0; i < n-1; i++)
cur = min(cur, 2 * x - a[i] - a[i+1] - abs(a[i] - a[i+1]));

total += cur;


cout << total << endl;
}
}