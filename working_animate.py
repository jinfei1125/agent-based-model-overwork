import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.animation as animation

def render(model):

    agent_types = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        if cell_content:
            cell_content = 1
        else:
            cell_content = 0
        agent_types[x][y] = cell_content

    return agent_types

def update(frameNum, img, model):
    model.step()
    img.set_data(render(model))
    return img

def animate(model):
    cmap = colors.ListedColormap(['grey', 'white'])
    formatter = plt.FuncFormatter(lambda val, loc: ['Workers', 'Empty'][loc])
    
    fig, ax = plt.subplots()
    img = ax.imshow(render(model), cmap=cmap)
    fig.colorbar(img, ticks=[0,1], format=formatter, ax=ax)
    ax.axis('off')
    
    plt.close()
    
    ani = animation.FuncAnimation(fig,
                                  update,
                                  fargs=(img, model,),
                                  frames=100, #100
                                  interval=100, #500
                                  save_count=100) #500
    return ani

def get_cumulative_revenue(model):
    return model.cumulative_revenue

def get_daily_revenue(model):
    return model.daily_revenue 

def get_turnover(model):
    return model.turnover 

def get_current_worker(model):
    return model.current_worker
