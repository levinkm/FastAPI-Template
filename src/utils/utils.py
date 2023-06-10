def response(res:any,details:str = "Success"):
    """response to be passed to the schema. Returns an object with results and details"""
    context= {
        "results" : res,
        "details" : details
    }
    return context

# customised pagination function

def paginate(res,pagination:dict,detail:str = "Success"):
    """paginates the results returning an object with results, pages links and details"""


    context = {
    "results": res[pagination['skip']:pagination['skip']+pagination['limit']],
    "pages": pagination["links"],
    "detail": detail

        }

    return context
