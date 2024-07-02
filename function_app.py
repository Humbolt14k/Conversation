import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="main")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP POST trigger function called main is processing a request')

    name_parameter = req.params.get('name')
    if not name_parameter:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name_parameter = req_body.get('name')

    if name_parameter:
        return func.HttpResponse(f"Hello, {name_parameter}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully",
             status_code=200
        )
    
@app.route(route="question")
def question(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP GET trigger function called question is processing a request')

    text_parameter = req.params.get('text')
    if text_parameter:
        if text_parameter.lower() == 'hi':
            return func.HttpResponse("How you doing?")
        elif text_parameter.lower() == 'bye':
            return func.HttpResponse("So long")
        else:
            return func.HttpResponse("Did not compute the text that was provided")
    else:
        return func.HttpResponse("Please provide a text parameter")
