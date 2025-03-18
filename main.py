# test HF models in here.
from transformers import pipeline

model = pipeline("summarization", model="facebook/bart-large-cnn")


extract = f"""
Public health plays a critical role in shaping a nation’s well-being and health-care delivery. The Constitution of India, through Article 47, underlines the state’s responsibility to improve public health care. Public health is a specialised field that requires specific knowledge and skills to effectively address people’s health needs. There is an urgent need for a dedicated workforce in India trained in public health, a fact that was very starkly realised during the COVID-19 pandemic. Beyond government systems, such a workforce is essential for civil society organisations, academic institutions, and research organisations engaged in public health.

The evolution of training and jobs in India
Though the surge in public health education in India is relatively recent, its history dates to the colonial era. In the early days, public health was largely embedded within medical teaching. This narrow approach persisted despite the establishment of the All India Institute of Hygiene and Public Health, Kolkata in 1932 and the subsequent inclusion of preventive and social medicine — later known as community medicine — as an essential part of medical education. Specialists in community medicine, well-trained in public health provided public health services and met human resource needs in this field. However, their numbers were limited, and they were often engaged in medical teaching. Many students pursued MPH courses abroad in countries such as Australia, the European Union, the United Kingdom and the U.S. Yet, the supply of public health professionals remained constrained. Recognising the growing need and demand, MPH institutions and teaching expanded in India.

The number of institutions offering MPH and related courses in India has grown rapidly. Currently, over 100 institutions offer master’s level courses in public health, whereas in 2000, there was only one. This expansion coincided with the launch of the National Rural Health Mission (NRHM) in 2005, which opened public health system roles to non-medical public health specialists. A wide range of institutions, from social science faculties to community medicine departments within medical institutions, have begun offering MPH courses. However, after an initial surge in demand, government recruitment for public health specialists plateaued, while the number of schools, programmes, and graduates continued to rise. As a result, securing jobs has become increasingly difficult for graduates.

Compounding this issue are challenges such as the lack of standardised training, insufficient practical learning opportunities, faculty shortages, and varied curricula that inadequately prepare students for real-world public health challenges. In addition, institutions offering public health courses are unevenly distributed, with large and populous States such as Assam, Bihar and Jharkhand, and many smaller and hilly States, having none or only a limited number of seats.


"""

response = model(extract)

print(response)
