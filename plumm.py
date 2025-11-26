
import asyncio
from summarizer import summarizer
from combiner import combiner
from splitter import split_transcript
import time

TXT = """
Sales Rep (SR): Hi Mark, this is Jamie from CloudConnect CRM. How are you today?

Buyer (B): Hi Jamie, I'm doing well, thanks. How about yourself?

SR: I'm great, thank you for asking! I appreciate you taking the time to speak with me today. To ensure our conversation is as valuable as possible for you, could you briefly share what prompted you to explore CRM solutions?

B: Sure, we've been using a basic CRM system, but it’s not keeping up with our growth. We’re missing features like advanced analytics and automation that can help us streamline our processes and improve customer engagement.

SR: That’s exactly what CloudConnect CRM is designed for. To give you a bit of background, our CRM is cloud-based, providing real-time access to data, which means your team can operate efficiently from anywhere. Do you currently face challenges with remote access to your CRM data?

B: Yes, that's a big issue, especially with some of our team working remotely. We need something more accessible and secure.

SR: I see, accessibility and security are foundational to our platform. We ensure that your data is not only easily accessible but also protected with the latest encryption standards. Let’s dive a bit deeper into the features. Are there specific sales processes you're looking to improve?

B: Well, our lead tracking is quite disjointed. We need a better system for monitoring interactions and following up on leads effectively.

SR: Our software excels in that area. CloudConnect CRM automates the lead tracking process, ensuring that every customer interaction is logged and analyzed. It can automatically assign tasks to the appropriate team members based on the customer's stage in the sales funnel. How do you currently handle task assignment?

B: It’s mostly manual, which leads to errors and missed opportunities.

SR: Automating these processes not only reduces errors but also frees up your team to focus on more strategic activities. Another feature that might interest you is our analytics dashboard, which provides actionable insights into sales performance. Would you find value in seeing a demo of how these features work?

B: Yes, that sounds helpful.

SR: Great! I’ll set up a screen share. [Proceeds with demo] Here you can see the dashboard. You can customize it to display key metrics like sales activity, pipeline health, and customer satisfaction scores. You can also set alerts for when sales drop below a certain threshold or when a high-value deal progresses. Does this visibility seem like it would benefit your team?

B: Absolutely, that looks very intuitive. Can it integrate with our existing systems?

SR: Yes, integration capabilities are a strong point for us. CloudConnect CRM can seamlessly integrate with your existing email, marketing automation, and customer service platforms. This ensures a unified view of each customer. What systems are you currently using?

B: We use Office 365 for most of our work, along with a couple of niche marketing tools.

SR: Perfect, we have plugins for Office 365 and an open API which can connect with virtually any software. This means you can keep using all your current tools without disruption. How does the pricing structure work for you in terms of budget?

B: Budget is tight as you can imagine; we're looking for high ROI.

SR: Understandable. Our pricing is tiered based on usage and features, starting at a competitive rate which I believe delivers excellent ROI given the improvements in efficiency and sales outcomes you can expect. I can send you a detailed proposal outlining the cost and benefits. Would that work for you?

B: Yes, please. Can you include a few case studies as well?

SR: Absolutely, I’ll include case studies from businesses similar to yours so you can see the real-world benefits. I'll email that over by the end of the day. Do you have any other questions?

B: Not right now, but I’m sure I will once I go through the proposal.

SR: Sounds good, Mark. I’ll be available for a follow-up call to discuss any questions you might have. Thanks again for your time today!

B: Thanks, Jamie. I look forward to your email.

SR: Have a great day, Mark. Bye!

B: Bye!


"""

if __name__ == "__main__":
    start_time = time.time()
    outputs, chunks = asyncio.run(summarizer(input=TXT))
    result = combiner(outputs)
    # Record the end time
    end_time = time.time()

    # Calculate and print the elapsed time
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(result)



        