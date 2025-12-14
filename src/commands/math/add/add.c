#include <stdio.h>

int main(void)
{
    int a, b, result;

    printf("Input two numbers: ");
    scanf("%d %d", &a, &b);

    // a + b = result 연산 수행 (어셈블리)
    asm
    (
        "movl %1, %%eax\n\t"    // a 값을 eax에 로드
        "addl %2, %%eax\n\t"    // eax에 b 값을 더함
        "movl %%eax, %0"    // 결과를 result에 저장
        : "=r" (result) // 출력: result
        : "r" (a), "r" (b)  // 입력: a, b
        : "eax" // 사용되는 레지스터
    );

    printf("%d + %d = %d\n", a, b, result);
    
    return 0;
}