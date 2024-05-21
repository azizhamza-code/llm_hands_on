# this repository is a collection of notes that I have taken to lean to work with llm abstraction and api


# lets start with langchain : 

-   langchain composes chains of components
        -   the way to do this by using what is called : LCEL chains, pipes, and Runnables. please refer to : https://www.pinecone.io/learn/series/langchain/langchain-expression-language/ a very good intro
-       in nutshell, LCEL and runnable protocols define a : 
        -   set of allowed of inputs and outputs types
        -   bunch of standard methods that all runnables will expose (like invoke, stream, batch, etc)


