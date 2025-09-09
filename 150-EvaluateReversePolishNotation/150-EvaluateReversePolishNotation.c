// Last updated: 09/09/2025, 14:19:55
int evalRPN(char** tokens, int tokensSize) {
    int st[10001];
    int top = -1;
  for(int i=0;i<tokensSize;i++){
//tokens[i]-->current strings"/"
//tokens[i][0]-->+,-,*,/-->operator
char ch = tokens[i][0];
int size = strlen(tokens[i]); // length of current string
//Operator(symbol) Case
if(size == 1 && (ch == '+' || ch == '-' || ch == '*' || ch == '/')) {
    int op2 = st[top];
    top--;
    int op1 = st[top];
    top--;
    int res;
    if(ch == '+') res = op1 + op2;
    else if(ch == '-') res = op1 - op2; 
    else if(ch == '*') res = op1 * op2;
    else if(ch == '/') res = op1 / op2;
    //push the res back in the stack
    st[++top] = res;
} else { //Operand (numbers) case
st[++top] = atoi(tokens[i]);
    // atoi()
}
}
  return st[top];
}