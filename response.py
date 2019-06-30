# Responses for Facebook
class SlackResponse(object):

    # class variable initializer initializer
    def __init__(self):
        self.platform = "slack"
    @staticmethod
    def response(text, button=[], seq=[]):
        
        return {"payload": {"slack": {"text": text, "attachments": button + seq}}}

    def text_response(self, texts):
        # text should contain at least one string
        if len(texts) <= 0:
            raise Exception("Provide the text for the text response")
        else:
            return texts

    def message_buttons(self, chips: list):
                        
        attachments = [
            {
                "text": "",
                "fallback": "Choose another options out of offer",
                "callback_id": "1",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "actions": [
                ]
            }
        ]
        for i in chips:
            temp = {
                "name": "options",
                "text": i,
                "type": "button",
                "value": i,
            }
            attachments[0]['actions'].append(temp)
        return attachments
        
    def recommend_seq(self, seq: list):

        attachments = [
            {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#36a64f",
            # "author_name": f"{texts}",
            "text": "Recommend next operations in sequence task",
            "fields": [            
                    ]
            }
        ]

        for i in seq:
            for key, value in i.items():
                temp = {
                        "title": key,
                        "value": value,
                        "short": False
                    }
                attachments[0]["fields"].append(temp)
        
        return attachments
# dialogflow fulfillment response
class fulfillment_response():

    def __init__(self):
        pass

    # fulfillment text builder
    # @param fulfillmentText = string
    def fulfillment_text(self, fulfillmentText):        
        if fulfillmentText == "":
            raise Exception("Fulfillment text should not be empty.")
        else:
            return {
                "fulfillment_text": str(fulfillmentText)
            }

    # fulfillment messages builder
    # @param response_objects (AOG response, FB response, Telegram response)
    def fulfillment_messages(self, response_objects):
        if len(response_objects) <= 0:
            raise Exception(
                "Response objects must contain at least one response object.")
        else:
            return {
                "fulfillment_messages": response_objects
            }

    # dialogflow output contexts
    # @param session = dialogflow session id
    # @param contexts = context name (string)
    def output_contexts(self, session, contexts):
        contexts_json = []
        for context in contexts:
            contexts_json.append({
                "name": session + "/contexts/" + context[0],
                "lifespanCount": context[1],
                "parameters": context[2]
            })

        # return the output context json
        return {
            "output_contexts": contexts_json
        }

    # dialogflow followup event JSON
    # @param name = event name
    # @param parameters = key value pair of parameters to be passed
    def followup_event_input(self, name, parameters):
        return {
            "followup_event_input": {
                "name": str(name),
                "parameters": parameters
            }
        }

    # main response with fulfillment text and fulfillment messages
    # @param fulfillment_text = fulfillment_text JSON
    # @param fulfillment_messages = fulfillment_messages JSON
    # @param output_contexts = output_contexts JSON
    # @param followup_event_input = followup_event_input JSON
    def main_response(self, fulfillment_text, fulfillment_messages=None, output_contexts=None, followup_event_input=None):
        if followup_event_input is not None:
            if output_contexts is not None:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages'],
                        "outputContexts": output_contexts['output_contexts'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "outputContexts": output_contexts['output_contexts'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
            else:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
        else:
            if output_contexts is not None:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages'],
                        "outputContexts": output_contexts['output_contexts']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "outputContexts": output_contexts['output_contexts']
                    }
            else:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text']
                    }

        # return the main dialogflow response
        return response