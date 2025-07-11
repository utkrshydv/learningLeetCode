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

        String result = sb.toString().replaceFirst("^0+", "");

        return result.isEmpty() ? "0" : result;
    }
}