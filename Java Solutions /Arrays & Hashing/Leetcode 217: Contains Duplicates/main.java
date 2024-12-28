public class main {
    // Brute Force Solution
    public boolean hasDuplicateBruteForce(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args)
    {
        // In java, you need to declare the "director" before you can access the "actor"...
        main sol1 = new main();

        int[] nums1 = {1, 2, 3, 3};
        int[] nums2 = {1, 2, 3, 4};

        // Once the director is declared, the actor can play his part...
        boolean num1 = sol1.hasDuplicateBruteForce(nums1);
        boolean num2 = sol1. hasDuplicateBruteForce(nums2); 

        System.out.printf("Nums 1 contains %s\n", num1);
        System.out.printf("Nums 2 contains %s\n", num2);

        
    }
}

