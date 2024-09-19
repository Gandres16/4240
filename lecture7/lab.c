#include <math.h>
#include <stdio.h>

int main()
{
    double number, result;

    printf("Enter a positive real number: ");
    scanf("%lf", &number);

    if (number <= 0) {
        printf("Error: Log of a non-positive number is undefined.\n");
        return 1; 
    }

    result = log(number);

    printf("Natural log of %.2lf is: %.5lf\n", number, result);

    return 0;
}