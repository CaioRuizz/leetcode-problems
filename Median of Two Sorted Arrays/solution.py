class Solution:
    def getMedian(self, nums1, nums2) : 
    
        i = 0 # index to iterati array 1
        j = 0 # index to iterate array 2
        m1, m2 = -1, -1 

        len_arr1 = len(nums1)
        len_arr2 = len(nums2)
    
        if((len_arr2 + len_arr1) % 2 == 1) :    
            for _ in range(((len_arr1 + len_arr2) // 2) + 1) :        
                if(i != len_arr1 and j != len_arr2) :            
                    if nums1[i] > nums2[j] :
                        m1 = nums2[j]
                        j += 1
                    else :
                        m1 = nums1[i]
                        i += 1            
                elif(i < len_arr1) :            
                    m1 = nums1[i]
                    i += 1
            
                # for case when j<m, 
                else :            
                    m1 = nums2[j]
                    j += 1        
            return m1
        
        else :
            for _ in range(((len_arr1 + len_arr2) // 2) + 1) :         
                m2 = m1
                if(i != len_arr1 and j != len_arr2) :        
                    if nums1[i] > nums2[j] :
                        m1 = nums2[j]
                        j += 1
                    else :
                        m1 = nums1[i]
                        i += 1            
                elif(i < len_arr1) :            
                    m1 = nums1[i]
                    i += 1

                else :            
                    m1 = nums2[j]
                    j += 1

            return (m1 + m2) / 2