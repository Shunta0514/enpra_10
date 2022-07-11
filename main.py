import sympy as sp

if __name__ == '__main__':
    theta_1 = sp.Symbol("theta_1")
    theta_2 = sp.Symbol("theta_2")
    theta_3 = sp.Symbol("theta_3")
    l_1 = sp.Symbol("L_1")
    l_2 = sp.Symbol("L_2")
    l_3 = sp.Symbol("L_3")
    l_4 = sp.Symbol("L_4")
    cTheta_1 =sp.cos(theta_1)
    sTheta_1 =sp.sin(theta_1)
    cTheta_2 = sp.cos(theta_2)
    sTheta_2 = sp.sin(theta_2)
    cTheta_3 = sp.cos(theta_3)
    sTheta_3 = sp.sin(theta_3)
    cTheta_23 = sp.cos(theta_2+theta_3)
    sTheta_23 = sp.sin(theta_2+theta_3)
    
    T0 = sp.Matrix([[cTheta_1,-sTheta_1,0,0 ],
                    [sTheta_1,cTheta_1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    T1 = sp.Matrix([[cTheta_2,-sTheta_2,0,0],
                    [0,0,-1,0],
                    [sTheta_2,cTheta_2,0,0],
                    [0,0,0,1]])
    T2 = sp.Matrix([[-cTheta_3,sTheta_3,0,l_1 ],
                    [-sTheta_3,-cTheta_3,0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    T3 = sp.Matrix([[sTheta_23,-cTheta_23,0,l_2 ],
                    [cTheta_23,sTheta_23,0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    T4 = sp.Matrix([[1,0,0,l_3],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    T5 = T0*T1*T2*T3*T4
    print(T5.col(3))