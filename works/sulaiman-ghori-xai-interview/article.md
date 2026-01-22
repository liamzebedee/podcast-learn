# WTF is Happening at xAI: An Interview with Sulaiman Ghori

*A conversation with an engineer at xAI about the company's culture, speed, and mission to build human emulators.*

---

## The Speed of xAI

**Tyler took this bet with Elon:** *"Get a Cybertruck tonight if you can get a training run on these GPUs in 24 hours."* And they were training that night. He got the Cybertruck.

*"My first day they just gave me a laptop and a badge and I was like, okay, now what? I don't even have a team. I've not been told what to do."*

That's how Sulaiman Ghori describes his first day at xAI. There was no formal onboarding. No assigned desk. He just sat at random people's desks that weren't there that day and started finding ways to contribute.

---

## No Blockers, No Bureaucracy

*"We don't have really due dates. It's always yesterday."*

The whole Elon philosophy of going down to the **root**—the fundamental, physical thing—applies even in software. There's no artificial blockers for anything. The company isn't fully a software company given all the infrastructure being built.

*"It's kind of hardware at this point,"* Ghori explains. *"It's like hardware constrained. It's probably our biggest edge—the hardware—because nobody else is even close on the deployment there."*

The talent density on software is unlike anywhere else. When they spin something up new, they quickly identify a **core metric**—usually tied to financial or physical return—and everything focuses on driving that metric.

---

## Challenging Conventional Limitations

*"There is a lot of perceived limitations, especially in the software world coming from the last 10 years of web dev. People just assume or accept certain limitations, especially when it comes to speed and latency—and they're not true."*

You can get rid of a lot of overhead. There's a lot of unnecessary complexity in the stack, and if you knock it out, you can usually **2x to 8x most anything** invented relatively recently.

The most recent example? Their model iterations on **Macro Hard**. They're working on novel architectures—multiple at the same time—and coming out with new iterations **daily**, sometimes multiple times a day. This is from pre-training in some cases, which is not something you ordinarily see.

*"Within a day of standing up a rack you can usually be training. Sometimes within the same day—even within a few hours in some cases."*

Normal timelines are days or weeks. In most cases over the last 10 years, companies abstract this away and let Amazon or Google handle it. But you can't have that be the case in AI now. *"The only solution is to die or build it yourself."*

---

## Joining xAI

Greg Yang, one of the co-founders, reached out to Ghori while he was working on his own startup. At first, Ghori thought it was spam.

*"I was going to mark it as spam to delete it. And I saw the domain x.ai. I was like, oh wait a second. I know these guys."*

After his startup didn't work out—it was fairly obvious you can't build Macro Hard with like a million dollars—he spent six or seven months on aerospace projects, including an astro mining concept. That also didn't work. So he emailed Greg again.

*"Hey, can you want to chat again?"*

*"Yeah, sure. You want to interview tomorrow?"*

He interviewed, did well, moved on Monday, and started. Nobody told him what to do.

---

## The Culture of Ownership

*"If I have a good idea, I can usually go and implement it that same day and show it to Elon or whoever and we got an answer."*

There's about three layers of management: ICs, co-founders/managers, and Elon. That's it. Because there's so few layers, nothing really comes top-down. Solutions usually bubble up from the bottom.

They did the math recently: they're at about **$2.5 million per commit** to the main repo. Ghori did five commits that day.

*"You added like 12 and a half million of value."*

*"The levers are extremely strong."*

---

## The Tesla Computer Play

One of the things xAI is thinking about: if they want to deploy 1 million human emulators, they need 1 million computers. How do they do that?

The answer showed up two days later in the form of **Tesla's in-car computer**. Those computers are actually very capital efficient. They can potentially run their model and the full computer environment a human would otherwise work at on the Tesla computer for much cheaper than on AWS or Oracle or even buying hardware from Nvidia.

*"There's like 4 million Tesla cars in North America alone. Let's say half of them have hardware 4. Somewhere between 70-80% of the time they're sitting there idle, probably charging. They have networking, they have cooling, they have power. We can just pay owners to lease time off their car and let us run a human emulator on it."*

No buildout required. Purely a software implementation.

---

## Macro Hard: The Human Emulator

**Macro Hard** is xAI's project to do for digital work what Optimus does for physical work.

*"With Optimus, you're taking any physical task a human can do and allowing a robot to do it automatically at a fraction of the cost with 24/7 uptime. We're doing the same with anything that a human does digitally."*

Anything where humans need to input keyboard and mouse inputs and look at a screen and make decisions—they just emulate what the human is doing directly. **No adoption from any software is required.** They can deploy in any situation a human is currently in.

The difference from going from 1,000 human emulators to a million is actually not very big. The infrastructure buildout has already happened.

---

## Elon's Problem-Solving Style

*"One of the things Elon does best is he basically just goes from fire to fire on whatever the company is and just puts it out and unfucks whatever problem exists."*

On the infrastructure side especially, there are specific operations each of the GPUs are built for. When they roll out new products from Nvidia, not everything works. In early meetings, Elon would hear about these issues, make a phone call, and the software team would deliver a patch **the next day**. They would work side by side until it was resolved, then run a training run very quickly—where otherwise it would have taken weeks of back and forth.

*"Those kind of blockers are usually very quickly resolved with one phone call."*

---

## Parallel Experimentation

*"Very frequently, we actually don't have a full picture until the all hands or we just chat with people about what everyone is doing."*

For example, when they did their voice model deployment, a lot of the work for extremely low latency was already built out—by someone else, for something else. It was a matter of flipping the right switches to cut latency 2-3x.

This happens a lot. There's something somewhere in the software or hardware, someone has already solved it, and you find it when you go looking.

*"There's not a lot of time spent syncing up with anyone or asking for permission or waiting for anyone at all. When you propose something, the answer is either 'no, that's dumb' or 'why isn't it done already?'"*

---

## Live by the Sword, Die by the Sword

*"You can kind of just ask for responsibility and then you basically just live by the sword, die by the sword. If you get things done, you can ask for more responsibility and keep doing that—or you're just out."*

Ghori has jumped around a lot of different projects, mostly because someone asked for his help and he kept helping, and then he ended up owning parts of the stack. There's no formal tracking—officially on HR software he's listed on voice and iOS, and the security software thinks he still works on the X integration.

*"Which never updated. No one ever updates this stuff."*

---

## The Three-Person iOS Team

*"Our iOS team is small for how many people use it. Like, it's ridiculous. You won't guess the number. It was three, and I was the third person when we were rolling that out."*

This is the first place where Ghori has had to work very hard to keep up with the speed and talent.

---

## The Imagine Rollout: 24-Hour Cycles

*"We had this 24-hour iteration cycle. We would all get feedback every night on whatever we were doing. And we would push out that night. In the morning we would have all the feedback. We would immediately knock out all the bugs, implement the new stuff that people were asking for. Whatever model had come up with, we implemented that too."*

It was the longest continuous stretch of him being in the office every day—two or three months with no weekends.

*"It was good to know that I could do that and I was pretty happy doing that."*

---

## Hiring Philosophy

They're doing hiring in unusual ways. Things that seemed stupid are okayed and tried. They'll do a hackathon, and if they get five people as a result, it's worth it—because the expected return on the company's revenue or valuation is higher than the cost.

For technical interviews, Ghori has a specific computer vision problem he solved years ago for a startup. He gives candidates half an hour to implement the solution.

*"It's actually very simple. A deceptively simple solution. People always overthink it. I like to index for: can you not overthink it and come up with a simple solution?"*

They're deploying on 30-40 years of different hardware and operating systems. You have to come up with simple solutions or you'll have a 10 million line codebase next week.

*"An AI will happily churn out 200 lines when a 10-line solution will do. I want people who can find the 10-line solution first."*

---

## Challenging Requirements

Chester, the Zai German, gave Ghori this idea: throw an **incorrect requirement** or impossible line into coding challenges. Expect candidates to come back and say "hey, this is wrong, this is not possible, you made a mistake." If they don't, don't hire them.

---

## Coming Up to Speed

*"If there's a lot of code to read—read the code by hand. Go to definition over and over again and you'll find things out very quickly."*

For things in active development, there might be 20 different versions going at the same time. You just have to talk to people. And people are very open.

*"I thought people would be super smart and stuck up, but no, people are just super smart and very nice and helpful. Everyone's on the same team, everyone's rooting for each other."*

They don't write a lot of docs. They do things too fast to write docs. They're trying to figure out systems to automatically generate docs as they build stuff—with Grok, which they have unlimited access to.

---

## The Speed of Iteration

*"You can always attempt to do something in one month that would otherwise take a year, and you'll probably get it done maybe in two. Still a lot faster."*

For Macro Hard specifically, they have pretty specific revenue targets. Whenever something gets delayed or accelerated, Ghori can quickly calculate how much money they just made or lost.

*"The numbers are huge. The timeline is so fast that a few days is actually proportionately fairly large."*

---

## The 1.5x Faster Decision

One of the biggest decisions made in a single meeting was to go with a model that would be **at least 1.5x faster than a human** for Macro Hard. It's looking like significantly faster than that—8x, maybe more.

*"For other human emulator attempts at other labs, the approach has been: let's do more reasoning and build a bigger model. That decision put us on totally the opposite track of what everyone else is doing."*

The analog is full self-driving. No one's going to wait around 10 minutes for the computer to do something they could have done in five. But if it can be done in 10 seconds? They'd be happy to pay whatever.

---

## Engineers, Not Researchers

Elon spent 10 minutes in one meeting going on about job descriptions: *"Engineers. Just engineers. Doesn't matter. Good engineers. Just someone who's fundamentally a problem solver. Doesn't matter if they did this XYZ thing in this infrastructure or this particular architecture. Engineers."*

Keeping it broad means people can come in from an extremely wide variety of places. There are stories at SpaceX of people who came in from strange walks of life and ended up doing huge things.

---

## No One Tells Me No

*"No one tells me no. If I have a good idea, I can usually go and implement it that same day and show it off. We'll run whatever eval or show it to a customer or show it to Elon or whoever and we'll get an answer usually that same day as to whether or not that was the right move. There's no deliberation. There's no waiting for any bureaucracy."*

---

## The Fuzzy Org Structure

*"The fuzziness between teams and what everyone is responsible for is definitely not what I expected and I don't think exists nearly as much in any large company."*

If Ghori needs to fix something on their VM infrastructure, he will do it. He'll show it to the person who owns that, they'll say okay, and it's merged immediately and deployed.

*"Everyone is allowed to update everything. There's some checks for dangerous things, but largely you're trusted to do the right thing and do it right."*

---

## The Delete-Then-Readd Pattern

Just like SpaceX and the algorithm, they delete things and add them back later.

*"Today. With Macro Hard, we deploy on a lot of physical hardware that changes. For example, with display scaling, we need to support displays that are 30 years old as well as the latest 5K Apple displays. I removed a special case for multiple encoders, turns out we found a problem at 5K+ resolution, so we added that back."*

---

## The Colossus Build

The lease for the land itself was actually **technically temporary**—it was the fastest way to get the permitting through and start building.

*"There's basically a special exception within local and state government that says if you want to modify this ground temporarily—I think it's for carnivals and stuff."*

xAI is technically a carnival company. That was the way to get things done. 122 days.

---

## Power Management

They have to collaborate very tightly with municipal and state power companies. When load goes high on their end, they have to shut off and go fully on 80+ mobile generators brought in on trucks—seamlessly, without interrupting anyone's extremely volatile training runs on extremely volatile hardware that scales up and down by **megawatts in milliseconds**.

The batteries can scale up and down and balance load much faster than generators. With a generator, you're asking a physical spinning thing to speed up or slow down. Batteries react to load much faster.

---

## Working Backwards

*"We try very hard to work backwards from: what's the highest leveraged thing we can be doing? Then we determine the physical requirements later."*

If they want to get to 10 or 100 billion in revenue by a certain date—what are the highest leverage things they can do economically? How can they build systems to do that? What does it take on the physical and software side? Roll backwards the whole way. They don't usually start with the physical requirement—that's at the end.

---

## The War Room

For Macro Hard specifically, they've been operating in a **war room for 4 months**. Yes, there's a sign on the door.

They actually outgrew the original war room and moved everything to the gym, which they cleared out and put everyone in.

---

## Virtual Employees and Disappearing Desks

They started testing human emulators internally as employees. In some cases, they didn't tell anyone.

*"Someone doing some work, and someone is like 'hey can you help me with this?' And the virtual employee is like 'yeah sure, come to my desk.' And they go there and there's nothing there."*

Multiple times Ghori has gotten a ping saying: *"Hey, this guy on the org chart reports to you. Is he not in today or something?"*

*"It's an AI. It's a virtual employee."*

---

## Finding Missing Steps

When working with customers on human emulators, they interview and document how humans do their jobs. A week later, they look at mistakes the virtual employee is making and realize there are 20 different steps missing that were just left out.

*"We go to them and they're like, 'oh yeah, we do that. I forgot to tell you. My bad.'"*

It happens all the time. People assume things automatically. Totally on autopilot. The same way you can be driving for an hour and not remember a single second of it.

---

## Generalization Surprises

*"Surprisingly, we've been able to generalize to more cases than we thought. Just today, we gave Elon a few cases where we did not train on this task at all, but it did it flawlessly—way better than we would have expected."*

The same parallel to full self-driving: stuff not in the training data that the car reacts to perfectly due to generalization of an otherwise very small model.

---

## Elon Meetings

*"They're pretty simple, honestly. Limited feedback or thumbs up means you're going in the right direction. Keep going. I'll hear updates next week. If there's feedback or a total reversal of direction as a request, then we messed up somewhere."*

Feedback is usually either at a very high level or at a very low level—not really in between. High level: product direction, customer focus, segment decisions. Low level: compute efficiency, latency, specific suggestions.

*"He's open to being proven wrong, but it has to be proof. It has to be: let's try it and see what the results are. It can't be just someone's opinion. There has to be an experiment done."*

---

## The Smaller Model Advantage

The compute efficiency of going with the smaller model has led to many improvements they wouldn't have otherwise thought of. Tesla found this too with full self-driving.

*"Going with the smaller model, they're able to iterate much faster. Not only does the model react to situations faster, you can also just deploy iterations much faster. If it was 4 weeks before, maybe it's one week now."*

That's why they can have 20 different experiments running in parallel.

---

## The Truth Problem

There's a lot of bias in Wikipedia. Elon has been focused on creating an alternate version that's more truthful.

*"It's a really hard problem. The internet is not usually the ground truth for whatever thing it is. Wherever we can, we try to drill down to the fundamentals—which is very hard."*

What are the fundamentals in physics of the Constitution? That's not really a question anyone could faithfully answer very well. But you try to drill down as close as you can and build up from that.

*"If anyone has suggestions, please send them through."*

---

## Why xAI Over SpaceX or Tesla

*"I'm definitely an entrepreneur by heart. xAI is definitely the smallest company, the newest of all of them. My assumption is—and this is largely proven true—where you can have the most leverage and change as an individual person, because proportionately you're a much larger percentage of the company."*

Another assumption that proved wrong: that he would be faster on his own to build things. He's actually usually faster at xAI because the groundwork and team have already done a lot of the steps he'd otherwise have to do by hand. And there's no one saying no.

---

## The Surge Nights

For the big models, surges happen where Elon comes in and people stay overnight. There are sleeping pods and bunk beds now.

*"And then when the tent picture came out, everyone kept sending that to me and I was like, honestly, yeah we have tents, but I've never seen that many out at once."*

One night, Elon walks into the war room and it's totally empty. "Where is everyone?" He walks over to where they are now—the gym—and conducts his impromptu questions.

*"That was a long night."*

---

## The Fidget Spinner Empire

As a kid, Ghori learned programming at 11 when his dad got him a book. He started liking it when he realized you could make money from it—writing game hacks and selling them online.

*"Making a couple hundred bucks online was huge for me. I remember having to ask my dad for a PayPal custody account. Getting the money in was like the coolest thing of all time."*

He saved up, bought parts for a 3D printer from Alibaba (RepRap style—build your own), assembled it at 3am on a school night, and one of the copper windings went 2 inches into his thumb.

*"It was a school night and it was like 3am because I wasn't very good at building things at 13. I spent like an hour in the bathroom trying to pull it out with tweezers and it just wasn't—it was bad. So I just cut it off."*

When the fidget spinner craze hit, he set up a little factory in his bedroom. Every two hours at night, he'd wake up and clear the print bed. Before school, he'd assemble them and sell at other bus stops through "distributors"—other kids at other schools.

After 2 months, he got shut down by the county. Official reason: the companies that sell school food have an exclusive license to sell anything on school property.

*"I think they just didn't like that I was distracting everyone and making money doing it. But it taught me a healthy disrespect for authority."*

---

## The Rocket Engine

Right before Thanksgiving, Ghori had been working on a liquid fuel rocket engine for four weeks. He bought textbooks and learned the design principles—material properties, chemical properties, machining, parameters, thrust output, how not to overpressure the engine.

*"The injector was very hard. That was probably 50% of the time."*

He was about to fly home for Thanksgiving. Either he builds it and fires it tonight, or he does it in two weeks.

*"I'm not going to do this in two weeks. I'm going to do this right now."*

He drank a lot of coffee, spent the whole day hacking away, and let it off that night.

The power supply hadn't come in yet to remotely power the onboard computer. He had to use a USB cable from his laptop. The longest one he had was 6 feet. So he had to stand right next to it and light it up.

*"There's like a 30% chance that this thing explodes or launches fire everywhere."*

The injector created a lot of overpressure events, which meant unburnt ethanol fuel spewing out. Some of it landed on his jacket and caught fire.

*"That's a trophy still, the burnt jacket."*

---

## Healthy Disrespect for Authority

*"I've always known from very young—I want an unconventional outcome. Going through a conventional path would pretty much necessarily not lead you to an unconventional outcome. So I grew opposed to any form of convention, and institutions necessarily enforce convention."*

*"Creativity and interesting outcomes come mostly from free-spirited individuals, in almost every case if not all of them. Staying true to that is the way to go."*

---

*Interview conducted by Relentless podcast*
