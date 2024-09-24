# Chat UI - Group 1
In order to speed up our development we decided that we would use a pre-build component for our visualization of our interactive chat.
For this there are currently a few possible tools, of which we have chosen Gradio to bootsrap our LLM.

# What is 'Gradio'
Gradio is a common standard python framework that is mainly used for fast prototyping and ideation.
The reason why it is often used is because it has some easy to use and integrate components that are used for all the common AI usecases.
On the huggingface hub, the GIT for AI models, they provide multiple demos using this framework aswel.


# Why are we using Gradio
As mentioned before, in the essence of saving time we decided to use pre build compoents.

If you take a look at our src.main file, you will find that running a chat intarface for example is as easy as calling:
'gr.ChatInterface().launch()'


# How do we integrate
If we have time, we would like to integrate this fully (probably with an Iframe) in our main frontend.
However the goal of this project is to create a simple interface that already works as intended to build further on.


