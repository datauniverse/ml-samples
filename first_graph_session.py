import tensorflow as tf

# TensorFlow define Variables
x = tf.Variable(3, name='x')
y = tf.Variable(4, name='y')

# TensorFlow define Function
f = x * x * y + y + 2


##### Simple Program that creates a session, initializes the variables and runs

# TensorFlow create Session
sess = tf.Session()

# Run the Session
sess.run(x.initializer)
sess.run(y.initializer) 
result = sess.run(f)

# Print the result
print(result)

# Close the session
sess.close()

##### Improvement 1: Use Session within a scope and make the code simple
with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    result = f.eval()
    print(result)

##### Improvement 2: Use a Global Variables Initializer for all variables
init = tf.global_variables_initializer()
with tf.Session() as sess:
    init.run() # Initialize all the variables
    result= f.eval()
    print(result)
    
##### Alternative of using Session is Interactive Session
##### Interactive Session with the default session within the Scope
##### Also remember to close the Session once it is complete
sess = tf.InteractiveSession()
init.run()
result = f.eval()
print(result)
sess.close()

##### Any node that you create is added to the default graph automatically
x1 = tf.Variable(1)
print(x1.graph is tf.get_default_graph()) # Should be True

##### You can create a new graph and make it the default within the scope
graph = tf.Graph()
with graph.as_default():
    x2 = tf.Variable(2)

print(x2.graph is graph) # Should be True
print(x2.graph is tf.get_default_graph()) # Should be False

##### TensorFlow determines the dependent nodes and evaluates them as required
w = tf.constant(3)
x = w + 2
y = x + 5
z = x * 3

with tf.Session() as sess:
    print(y.eval()) # Should print 10
    print(z.eval()) # Should print 15
    

    
