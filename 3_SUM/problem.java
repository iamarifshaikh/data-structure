import java.util.*;

public class problem{
    public static List<List<Integer>> findTriplets(int[] nums){
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int i = 0;
        
        while (i < nums.length){
            int j = i + 1;
            int k = nums.length - 1;

            if (i > 0 && nums[i] == nums[i -1]){
                i += 1;
                continue;        
            }

            while (j < k){
                int triplets = nums[i] + nums[j] + nums[k];

                if (triplets == 0){
                    result.add(Arrays.asList(nums[i],nums[j],nums[k]));
                    j += 1;

                    // while(j < k && nums[j] == nums[j - 1]) j+= 1;
                    // while(k > j && nums[k] == nums[k + 1]) k-= 1;

                }else if (triplets > 0) {
                    k -= 1;
                }else{
                    j += 1;
                }

            }
            i++ ;
        }
        return result;
    };
    public static void main(String[] args){
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = findTriplets(nums);
         for (List<Integer> triplet : result) {
            System.out.println(triplet);
        }
    }
}