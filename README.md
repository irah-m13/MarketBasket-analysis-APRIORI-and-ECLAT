# Market Basket Analysis Using APRIORI and ECLAT

In this project, we use APRIORI and ECLAT for identifying the buying pattern to increase sales - Association with items. 
Example : If a customer buy bread then find whether they will buy butter along with it. If a customer buy bread and butter will the customer buy ketchup along with it.                                                                                                                                 

ARIORI :                                                                                                                                   
     -- Works in horizontal manner imitating Breadth First Search.(slower compared with ECLAT).                                                            
     -- Has antecedent and Consequent as Lhs and rhs.                                                        
     -- Has Support, Confidence , Lift and Conviction.                                                        
ECLAT :                                                                                                                                  
     -- Equivalence class clustering and bottom-up lattice traversal algorithm                                                        
     -- Works in vetrical manner like Depth First Search and faster than APRIORI.                                                        
     -- Does not need repeated scanning and has onl consequent.                                                        
     -- Has only Support and Confidence.                                                        
        
        
        
Procedure of APRIORI :                                                                                                                   
=> Analyse the problem that is need to be found, here we need to identify association or pattern behind item brought by customers.                         
=> Importing dataset of sales report.                                                                                                                            => Summarize dataset..                                                                                                  
=> Create rating matix of shape(m x u).                                                                                                  
=> Implement APRIORI algorithm by antecedent and conseguent means.                                                                                           
=> In order for selection consider support, confidence, lift, conviction.                                                                                        => Data Preprocessing is carried.                                                                                                  
=> Train dataset using APRIORI.                                                                                                  
=> Obtain result in DataFrame format.                                                                                                  

        
Procedure of ECLAT :                                                                                                                                    
=> Analyse the problem that is need to be found, here we need to identify association or pattern behind item brought by customers.                        
=> Importing dataset of sales report.                                                                                                                            => Summarize dataset..                                                                                                  
=> Create rating matix of shape(m x u).                                                                                                  
=> Implement ECLAT algorithm by conseguent means.                                                                                           
=> In order for selection consider support, confidence.                                                                                                         => Data Preprocessing is carried.                                                                                                  
=> Train dataset using ECLAT.                                                                                                  
=> Obtain result in DataFrame format.                                                         

