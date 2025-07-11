class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();

        for(char digit : num.toCharArray()){
            while(!stack.isEmpty() && k > 0 && stack.peek() > digit){
                stack.pop();
                k--;
            }
            stack.push(digit);
        }

        while(k>0 && !stack.isEmpty()){
            stack.pop();
            k--;
        }

        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }

        sb.reverse();

        int firstNonZeroIndex = 0;
        while(firstNonZeroIndex < sb.length() -1 && sb.charAt(firstNonZeroIndex) == '0'){
            firstNonZeroIndex++;
        }

        String result = sb.substring(firstNonZeroIndex);

        if(result.isEmpty()){
            return "0";
        }

        return result;
    }
}