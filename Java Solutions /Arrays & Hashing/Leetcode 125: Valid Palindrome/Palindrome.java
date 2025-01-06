public class Palindrome {
    /*
    Given a string s, return true if it is a palindrome, otherwise return false.
    A palindrome is a string that reads the same forward and backward. 
    It is also case-insensitive and ignores all non-alphanumeric characters.
    
    If it reads the same way after its been reversed, its a palindrome....

    Filter out the blank spaces 
     */

        //Build the string, check the char in s.
    public boolean isPalinReverseString(String s) 
        {
           // Build a new string, at the cost of extra memory.
           StringBuilder newStr = new StringBuilder(); 
   
           for(char c: s.toCharArray())
           {
               // If the character is alphanumeric
               if (Character.isLetterOrDigit(c)) 
               {
                   //Append the character to newStr, in lower case letters  
                   newStr.append(Character.toLowerCase(c));
               }
           }
           return newStr.toString().equals(newStr.reverse().toString());
        }
    

    public boolean isPalinTwoPointers(String s)
    {
        int l = 0, r = s.length() - 1; 

        while (l < r)
        {
            while (l < r && !alphaNum(s.charAt(l)))
            {
                l++;
            }
            while (r > l && !alphaNum(s.charAt(r)))
            {
                r --; 
            }
            if (Character.toLowerCase(s.charAt(l)) != 
                Character.toLowerCase(s.charAt(r)))
                {

                    return false; 

                }
                l ++; r--; 
        }
        return true; 
    }


    public boolean alphaNum(char c)
    {

        return(c >= 'A' && c <= 'Z' || 
               c >= 'a' && c <= 'z' || 
               c >= '0' && c <= '9');

    }

    public void output()
    {
        Palindrome sol = new Palindrome(); 

        String s1 = "Was it a car or a cat I saw?"; String s2 = "tab a cat"; 

        Boolean solution1 = sol.isPalinReverseString(s1); Boolean solution2 = sol.isPalinReverseString(s2); 
        Boolean solution3 = sol.isPalinTwoPointers(s1); Boolean solution4 = sol.isPalinTwoPointers(s2); 

        System.out.println("Is Valid Palindrome (Using Sorting Algo): ");
        System.out.printf("The following string '%s' is a Palindrome: %s\n", s1, solution1);
        System.out.printf("The following string '%s' is a Palindrome: %s\n", s2, solution2);
        System.out.println();

        System.out.println("Is Valid Palindrome (Using Two Pointers): ");
        System.out.printf("The following string '%s' is a Palindrome: %s\n", s1, solution3);
        System.out.printf("The following string '%s' is a Palindrome: %s\n", s2, solution4);

    }

}

   