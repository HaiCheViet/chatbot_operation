# Responses for Facebook
class SlackResponse(object):

    # class variable initializer initializer
    def __init__(self):
        self.platform = "slack"

    def text_response(self, texts):
        # text should contain at least one string
        if len(texts) <= 0:
            raise Exception("Provide the text for the text response")
        else:
            # text_obj list for storing the text variations
            text_obj = []
            for text in texts:
                text_obj.append(str(text))

            # return the text response
            return {
                "text": {
                    "text": text_obj
                },
                "platform": self.platform
            }

    def message_buttons(self, texts, attachment):
        if len(texts) <= 0:
            raise Exception("Provide the text for the text response")
        else:
            attachments = [
                {
                    "text": "Choose these options below",
                    "fallback": "Choose another options out of offer",
                    "callback_id": "wopr_game",
                    "color": "#3AA3E3",
                    "attachment_type": "default",
                    "actions": [
                    ]
                }
            ]
            for i in attachments:
                temp = {
                    "name": "options",
                    "text": i["text"],
                    "type": "button",
                    "value": i["value"],
                }
                attachments
        return {
            "text": texts,
            "attachments":
        }

    def quick_replies(self, title, quick_replies_list):
        if title == "":
            raise Exception("Title is required for basic card in facebook.")
        # quick_replies_list must contains at least one string
        elif len(quick_replies_list) <= 0:
            raise Exception(
                "Quick replies response must contain at least on text string.")
        else:
            # quick replies list to store the quick replie text
            quick_replies = []
            for quick_reply in quick_replies_list:
                # append to the list
                quick_replies.append(
                    str(quick_reply)
                )

            # return the response JSON
            return {
                "quickReplies": {
                    "title": str(title),
                    "quickReplies": quick_replies
                },
                "platform": self.platform
            }

    def card_response(self, title, buttons):
        buttons_json = []
        for button in buttons:
            buttons_json.append(
                {
                    "text": str(button[0]),
                    "postback": str(button[1])
                }
            )

        # return the card
        return {
            "card": {
                "title": str(title),
                "buttons": buttons_json
            },
            "platform": self.platform
        }
