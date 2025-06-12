class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;

        do{
            slow = sumOfDigits(slow);
            fast = sumOfDigits(sumOfDigits(fast));
        } while(slow != fast);

        return slow == 1 ? true : false;
        
    }

    static int sumOfDigits(int num){
        int sum = 0;
        while(num > 0){
            int digit = num%10;
            sum  += digit * digit;
            num = num /10;
        }
        return sum;
    }
}