#include <cstdio>

using namespace std;

const int MAXN = 1050;
int a[MAXN], b[MAXN];

int gcd(int a, int b){
    if (b == 0) return a;
    return gcd(b, a%b);
}

int main(){
    // printf("hello, world\n");
    freopen("in.txt", "r", stdin);
    int T=0; scanf("%d", &T);
    for (int r=0; r < T; r ++) {
        // printf("r %d\n", r);
        int n; scanf("%d", &n);
        for (int i=0; i < n; i++) scanf("%d", &a[i]);
        for (int i=0; i < n; i++) scanf("%d", &b[i]);
        for (int j=n-1; j >= 0; j--) {
            if (a[j] == 0 && b[j] == 0) continue;
            int p = a[j], q = b[j];
            if (p == 0) {printf("0/1\n");break;}
            else if (q == 0) {printf("1/0\n");break;}
            else {
                int g = gcd(p, q);
                printf("%d/%d\n", p/g, q/g);
                break;
            }
        }

    }

}
