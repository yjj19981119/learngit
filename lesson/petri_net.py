import numpy as np

class Petri():
    def __init__(self,mat_pre,mat_post,m0):
        self.mat_pre =mat_pre
        self.mat_post =mat_post
        self.mat=self.mat_post-self.mat_pre
        self.m =m0

    def is_transition(self):
        self.tran=(self.m[:,np.newaxis]>=self.mat_pre).all(0).nonzero()[0]
    
    def firing(self,T):
        self.m = self.m + self.mat[:,T]
    
        
def main():
    mat_pre = np.loadtxt("c.pre.txt")
    mat_post = np.loadtxt("c.post.txt")
    m0 = np.loadtxt("m0.txt")
    petri_net=Petri(mat_pre,mat_post,m0)
    print(petri_net.mat)
    print("当前标识：",petri_net.m)
    print("库所数：",petri_net.mat.shape[0])
    print("变迁数：",petri_net.mat.shape[1])
    for x in range(5):
        petri_net.is_transition()  #判断变迁是否可激发
        print("\n可激发的变迁：",[y+1 for y in petri_net.tran])  
        tran_enable=np.random.choice(petri_net.tran)  #随机选择可激发的变迁
        petri_net.firing(tran_enable)    #激发变迁
        print("激发变迁：",tran_enable+1)
        print("当前标识：",petri_net.m)

if __name__ == "__main__":
    main()
