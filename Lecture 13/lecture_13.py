def get_partial_deriv_m(points, m, c):
    ans = 0
    for pnt in points:
        ans += pnt[0] * (pnt[1] - (m * pnt[0]) - c)
    ans = ans * (-2/len(points))
    return ans

def get_partial_deriv_c(points, m, c):
    ans = 0
    for pnt in points:
        ans += pnt[1] - (m * pnt[0]) - c
    ans = ans * (-2/len(points))
    return ans

def get_J(points, m, c):
    ans = 0
    for pnt in points:
        ans += (pnt[1] - (m * pnt[0] + c))**2
    ans /= len(points)
    return ans

def get_regression_eq(points, m, c, alpha, max_iter, min_J):
    for i in range(max_iter):
        J = get_J(points, m, c)
        if J <= min_J:
            return m, c
        
        m_deriv = get_partial_deriv_m(points, m, c)
        c_deriv = get_partial_deriv_c(points, m, c)
        m = m - alpha * m_deriv
        c = c - alpha * c_deriv
        print("Iter {0}: m = {1}, c = {2}, J = {3}".format(i+1, m, c, J))
    return m, c
        

points = [ [0,0], [0.1,0.1], [0.15,0.2], [0.2,0.1], [0.25,0.15], [0.3,0.25] ]

# alpha is learning rate
alpha = 0.01

# max iterations for gradient descent before terminating
max_iter = 10000

# minimum J for optimal line
min_J = 0.0001

starting_m = 0
starting_c = 0
m, c = get_regression_eq(points, starting_m, starting_c, alpha, max_iter, min_J)

print("y = {0}x + {1}".format(m,c))