Dr David C. Klonoff
Editor in Chief, Journal of Diabetes Science and Technology

Dear Dr Klonoff,

I am submitting an original article, "A paid application standardises what large language models read about insulin pump settings and leaves what they decide to chance: reproducibility of an automated insulin delivery settings review across eleven models", for consideration by the Journal of Diabetes Science and Technology.

The study concerns a commercial Android application that packages a user's Nightscout and AndroidAPS data with four fixed prompts for pasting into any large language model, checks the returned JSON and presents it as a settings review. I replayed the application's workflow, with its own package and prompts, against eleven models from six providers in fresh conversations, 50 per model where cost allowed, on a single 14-day record, and judged every response with a validator reconstructed from the application's behaviour and verified against it on 25 pasted outputs. The models quoted the record accurately and then disagreed about what to change, between models and within them, while the application's check, which inspects the structure of the answer and not its content, accepted the lot.

The single-record design is deliberate rather than a constraint. The question is whether the same input produces the same review; holding the record fixed while the conversation is repeated attributes all of the observed variation to the model and the application. Whether any of the reviews was correct is a different question requiring many records and a reference standard, and the paper does not claim to answer it; the concern it raises is that the user is given no means of telling one answer from another.

A companion commentary, "Is an application that prepares your data and prompts for a chatbot a medical device?", is submitted alongside this article and is referred to in it; the two are written to stand alone but are best read together, and I would be glad for them to be handled as a pair. The harness, validator, analysis code, prompts, every transcript and model output, and the study package with identifiers removed are released in a public repository, and the supplementary tables give the model identifier each provider returned for every conversation, the full validator verification, and a per-decision check of whether each change's rationale cites a figure from the record, and analyses of how each model read the package's bolus-only insulin total and its other partial fields.

Since the manuscripts were completed, the developer has withdrawn the application from Google Play, confirming to me that the withdrawal followed publication of these findings; both manuscripts note this, and the analysis describes the product as it was sold.

In line with the journal's policy on prior posting, both pieces have been posted as preprints, both on Zenodo (original article [DOI 1]; commentary [DOI 2]), and on diabettech.com; no updated version will be posted while the manuscripts are under review.

The data analysed are my own. I run Diabettech Ltd, sit on the committee of the Diabetes Technology Network UK and wrote its statement on large language models, and I am the author of the two preprints the article cites. I have no relationship with the developer of the application and paid for its subscription. The work received no funding.

Reviewers able to assess both the diabetes technology and the evaluation of language models would be best placed to judge the paper; I can suggest names if that would help.

Yours faithfully,

Tim Street, MEng BEng (Hons)
Diabettech Ltd, 44 Brandram Road, London SE13 5RT, United Kingdom
+44 7740 051 460, tim@diabettech.com
