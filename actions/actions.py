# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionProcessarTipoDocumento(Action):

    def name(self) -> Text:
        return "action_processar_tipo_documento"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        documento = tracker.get_slot("documento")
        print("Documento: " + documento)

        tipo_documento = tracker.get_slot("tipo_documento")
        print("Tipo de documento: " + tipo_documento)

        nome_documento = ""

        if documento == "atestado_matricula":
            nome_documento = "Atestado de matrícula"
        elif documento == "atestado_frequencia":
            nome_documento = "Atestado de frequência"
        else:
            dispatcher.utter_message(text=f"Desculpe, não consegui entender que tipo de documento você quer. Você poderia tentar de novo?")
            return []
        
        if tipo_documento == "digital":
            dispatcher.utter_message(text=f"Certo. Para emitir o seu {nome_documento} a partir do SIGAA, siga os passos abaixo:")
            dispatcher.utter_message(text=f"- Primeiro acesse o [SIGAA](https://sigaa.ifsc.edu.br) utilizando seu login e senha; Ao acessar o SIGAA, no menu superior, clique em \"Ensino\" e, em seguida, em \"{nome_documento}\".")
            dispatcher.utter_message(text=f"- Então,  o seu {nome_documento} será aberto em uma nova janela. Você pode imprimi-lo ou salvá-lo através do botão “imprimir” no final da página.")
        else:
            dispatcher.utter_message(text=f"Beleza. Para receber o seu {nome_documento} impresso com carimbo e assinatura, você deve ir à secretaria do IFSC Campus Gaspar pessoalmente. O horário de atendimento é de segunda a sexta-feira, das 8h às 20h.")

        return []
