
import java.util.Arrays;

public class main {
    public int[] twoSumBruteForce(int[] nums, int target){
        for (int i = 0; i < nums.length; i++)
        {
            for(int j = i; j < nums.length;j++)
            {
                if(nums[i] + nums[j] == target)
                {
                    return new int[]{i, j}; 
                }
            }
        }
        return new int[0]; 
    }

    public static void main(String[] args) {
        print(); 

    }
    public static void print(){
        main solution = new main(); 

        int[] nums1 = {3,4,5,6};
        int[] nums2 = {4,5,6};
        int target1 = 7; 
        int target2 = 10; 

        int[] sol1 = solution.twoSumBruteForce(nums1, target1); 
        int[] sol2 = solution.twoSumBruteForce(nums2, target2); 


        System.out.printf("The two values that add up to target '%d' is %s%n", target1, Arrays.toString(sol1));
        System.out.printf("The two values that add up to target '%d' is %s%n", target2, Arrays.toString(sol2));
    }
}
