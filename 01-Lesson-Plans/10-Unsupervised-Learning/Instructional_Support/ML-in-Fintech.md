# Machine Learning in Fintech Today

Machine learning is the backbone of the majority of fintech business models. This is because large amounts of data and fast, cheap decisions about what to do with that data underpin a lot of the value proposition that fintech firms can offer. And the fast, cheap analysis of lots of data is the specialised purview of the field of machine learning (ML).

In this module, the students will get the why, where, and how of ML. _Why_, because they (and you) will want to know more about why machine learning is commonly deployed in the industry, and therefore a relevant skill for their careers. Similarly, the students will want to know the _where_ to sharpen their industry awareness and know which companies use machine learning. Last, but most important, they’ll learn _how_ to do ML, with many opportunities to write Python code to build machine learning models and make predictions.

In this guide to machine learning, we’ll examine the why, where, and how of ML more closely.

## The Why: Why ML Is Essential for Fintech

Machine learning is applied in a variety of ways, such as textual analysis of fraudulent contracts, determining interest rates and [whether to lend on](https://blogs.thomsonreuters.com/answerson/sofis-data-science-head-opening-the-funnel-to-non-traditional-borrowers-with-machine-learning/) loans, and automated trading models.

One interesting application of machine learning is how it’s being used to replace traditional financial advisors with artificial intelligence (AI). [Wealthfront](https://www.wealthfront.com/methodology), [Betterment](https://www.betterment.com/category/engineering/), and [SoFi](https://www.sofi.com/learn/content/what-is-an-automated-advisor/) ("Social Finance") are examples of fintech that automate part or all of the process for saving for retirement. Using ML to recommend tailored portfolios and manage the whole process means that customers no longer have to pay high annual fees to traditional advisors. And, after all, millennials and later generations [would rather talk to a screen](https://tearsheet.co/future-of-investing/our-clientele-pay-us-not-to-talk-to-them-wealthfront-ceo-andy-rachleff-on-why-robos-dont-need-humans/) than a person when it comes to their finances.

Automation to reduce costs is not isolated to fintech products that are oriented toward end users, such as individuals saving for retirement. JP Morgan, for example, has [written a program called COIN](https://digital.hbs.edu/platform-rctom/submission/jp-morgan-coin-a-banks-side-project-spells-disruption-for-the-legal-industry/), which uses natural language processing (NLP) to automatically run due diligence on all of its commercial credit contract agreements. These lines of code have compressed what previously was 360,000 hours of work done by humans into seconds.

Sometimes, what really matters is the combination of natural language processing, or NLP, and the pattern recognition abilities of various other ML algorithms, like random forests (in the machine learning modules, you'll learn how to do both of these).

Insurance companies, for example, attempt to lower costs by [putting NLP-driven chatbots into the insurance claim process](https://www.spixii.com/success-stories/zurich-case-study). This way, the long process of filing a claim, presenting evidence via uploaded photos, and settling payments are done largely without the help of a specialist claims adjuster. Along with the chatbots, ML is used throughout this process to flag potentially fraudulent claims or a dissatisfied customer.

Consider again fintech’s role in dispensing financial advice and overseeing savings. NLP can replace the (traditionally human) financial advisor by asking questions pertaining to tolerated risk, ability to save, or when they want to retire. For banks seeking to automate financial advising, [they’d likely involve an NLP chatbot](https://medium.com/botique-ai/conversational-banking-chatbots-the-future-of-banks-in-the-age-of-digital-disruption-3f776a0d3ad3) to extract the answers from the potential customer, and another machine learning model (random forests, KNN, or a DNN) behind the scenes. This latter model would correlate data on the bank’s past customers with the various financial products those customers primarily chose. The bank would then [use that ML model to infer those statistical relationships](https://www.bbva.com/en/machine-learning-how-its-used-in-banking/). The NLP chatbot would then use those findings in order to allow it to inform new customers about what types of financial products they might be interested in.

NLP in fintech can get quite sophisticated. For example, consider the level of NLP behind these two fintechs, [Alphasense](https://www.alpha-sense.com/) and [DataMinr](https://www.dataminr.com/). Essentially, these are global news monitoring APIs, subscribed to by large asset managers and banks in order to help them track relevant risk related information. The two firms get paid in order to (algorithmically) conduct real-time monitoring and textual analysis of _everything_ written about _any_ firm. Sources are disparate, ranging from financial filings, tweets, press releases, investor conferences, regulatory filings. Imagine, for example, how valuable it would be for a hedge fund that could monitor different drug companies in real time; perhaps whether they’ve just filed FDA results, presented findings at a conference, or published financial information with the SEC. The financial advantage to faster information is enormous, and is one reason why [DataMinr alone](https://www.crunchbase.com/organization/dataminr#section-overview) is worth more than $1 billion.

On that point, let’s not forget the scope for applying ML models to forecast financial market results. These forecasts range from loan evaluation (for example, predicting default rates on bonds or consumer loans) to high-frequency algorithmic trading in the stock market.

Algorithmic trading driven by statistical models is not necessarily new— the quant hedge fund known as [TwoSigma](https://twosigmasecurities.com/), for example, automatically trades more than 300 million shares a day (or about one share for every person in the U.S., per day). The fund has been in the business since the early 2000s. However, within the last five years, algorithmic trading—including of the variety driven by decisions involving ML—now accounts for [between 75% to 90%](https://en.wikipedia.org/wiki/Automated_trading_system) of all equity trades in the U.S. What's more, perhaps in part by their purely virtual beginnings, more cryptocurrency exchanges and trading firms are looking for individuals that can write ML code that trades profitably.

Outside of the equity market, ML is used to classify good lending decisions from bad. This can take the form of algorithmic hedge funds that trade bonds, but more commonly involves the instant and automated assessment of the quality of a potential loan. From credit whales like [Wells Fargo](https://databricks.com/session/productionizing-credit-risk-analytics-with-lstm-tensorspark-a-wells-fargo-case-study) to smaller peer-to-peer players like [LendingClub](https://www.lendingclub.com/), ML algorithms—-and not loan officers-—are what decides who gets a loan and on what terms (like maturity or interest rate). The gist behind this application of ML models is that they correlate data on past customer characteristics and payment history to find, and thus predict, the patterns that lead to non-payment (default). With better and cheaper predictions, the end result is a lower loss rate to the lender, and ultimately lower rates overall to borrowers.

The use of ML in fintech today is more extensive than this guide can cover. Other uses not already mentioned include firms [built to identify money laundering](https://www.conpend.com/trafinas/) or sanctions violations, satellite recognition for real-time awareness of trading opportunities in commodities, and the prediction of customer churn in financial products. Even the [venture capital](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/a-machine-learning-approach-to-venture-capital) and [private equity](https://knowledge.wharton.upenn.edu/article/data-analytics-slowly-transforming-private-equity/) industries have begun to experiment with ML models to predict the likelihood of start-up success. As long as there is something to automate or something to predict, ML is there. The potential applications are vast.

## The Where: Fintechs That Use ML (and the Skills They’re Hiring for)

In addition to the firms mentioned in the previous section, here are a few examples of fintechs doing primarily ML. There are thousands more listed at Crunchbase if you'd like to explore this topic further.

### Sift

[Sift](https://www.sift.com/), with Crunchbase funding of [106 million](https://www.crunchbase.com/organization/sift-science#section-overview):

Founded in 2011, this fintech supplies ML algorithms that can predict and thus prevent detrimental transactions like fake account signups, stolen credit cards, and other scams. Basically, the firm’s ML models take datasets filled with users’ browser and internet protocol (IP) data across multiple websites, along with thousands of other characteristics, and use that data to separate genuine orders and customers and transactions from fraudulent records (e.g., by preventing chargebacks, customers with a history of blocked accounts, and so on). Customers who buy their models range from transaction processors as big as Jet (owned by Walmart) and AirBnB, to companies that are sensitive to a lot of fraud via natural language, like Twitter and Twilio (a developer backend for language processing in apps).

Sample [jobs](https://sift.com/careers) at Sift include the following:

* Senior Solutions Engineer: This role involves understanding Sift’s machine learning models, and tracking the data flow, as well as scripting internal tools and working with the API.

* Support Engineer: This role requires background working with API based products, as well as  experience scripting in Python, Ruby, or other languages.

### States Title

[States Title](https://statestitle.com/), an "insurtech" firm with Crunchbase funding of [106.6M](https://www.crunchbase.com/organization/states-title#section-overview)

In what is typically a sizable ($25 billion) industry, but rather staid and paperwork-driven, this firm is disrupting the insurtech industry by applying machine learning models to detect and understand written language. Specifically, this firm automates a lot of paperwork surrounding real-estate transactions and uses ML to spot potential human mistakes in the process. (It’s confident enough in the uniqueness of its application of ML that it's actually [patented the process](https://statestitle.com/resource/states-title-awarded-machine-intelligence-patent/).

Sample [jobs](https://statestitle.com/team-careers/) at States Title include the following:

* Data Engineer: This role requires experience with scripting languages, such as Python, as well as experience with cloud services such as Azure. The ideal candidate should also be familiar with machine learning concepts, such as supervised learning, and frameworks such as scikit-learn.

* Data Analyst: This position is focused on data analytics, business intelligence, or data science projects. Candidates should be able to write complex SQL joins and to analyse datasets by using Python.

In these ML modules, the students will get plenty of opportunities to write Python code and deploy some of these ML frameworks to cloud services like Microsoft’s Azure, Google Cloud, and Amazon AWS).

### FundBox

[FundBox](https://fundbox.com/), a B2B fintech with Crunchbase funding of [433.5M](https://www.crunchbase.com/organization/fundbox):

This firm is a B2B firm, meaning it sells its products directly to other businesses. Therefore, it’s not a household name. Despite that, it’s raised nearly a half billion dollars in venture capital.

Businesses typically pay each other after 30 days, not immediately like a normal consumer transaction, such as a person buying groceries at a grocery store. But small businesses typically don’t want to wait that long to receive their money: if they have their money earlier, they can buy new raw material, pay bills, and generally put it to work more quickly. Fundbox therefore lends money to small-to-medium businesses (SMBs) in a process known as “factoring”.

Factoring is when firms get loans backed by sales already made but not yet collected on (“accounts receivables”). Because of the thicket of regulation, though, Fundbox doesn’t actually make the loans themselves. Like many fintech lenders, Fundbox is more of an intermediary; it contracts with an underlying bank (typically a small one, like a credit union) when it comes time to supply the money to the customer, taking a fee along the way for its matchmaking and credit evaluating service.

As for machine learning, the firm builds proprietary machine learning models to predict the individual credit risk of those firms that apply for money to borrow. Because of the predictive accuracy of their models, the firm can offer businesses lower interest rates for loans without experiencing higher defaults.

Sample [jobs](https://statestitle.com/team-careers/) include the following:

* Senior Credit Analyst: A person in this role should be skilled in database management (SQL), R and Python, as well as modelling in Excel. This role will work closely with the Data Science team to leverage new risk models in underwriting.

* Fraud Analyst: The person in this role will complete independent research projects. SQL/Python knowledge is preferred, but not required.

* Data Analyst: This person in this position will recommend actionable insights and strategies based on data analysis. Experience with database management is required, and familiarity with R / Python is a plus.

## The How: How the Students Will Learn to Use ML Code

This is your specialty. Using the instructor demos and in-class activities for Modules 10–17, it’ll be up to you to get the students writing ML code and making predictions from ML models.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
