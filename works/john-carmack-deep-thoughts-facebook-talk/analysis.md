# Analysis: John Carmack at Facebook's "Deep Thoughts Engineering Speaker Series"

**Host:** Kent Beck
**Speaker:** John Carmack (CTO of Oculus VR at the time)
**Topic:** Ideas and Engineering

---

## Executive Summary

This talk, hosted by Kent Beck as part of Facebook's inaugural "Deep Thoughts Engineering Speaker Series," features John Carmack discussing his philosophy on ideas in engineering. Rather than celebrating the romantic notion of brilliant "eureka moments," Carmack argues that ideas are vastly overvalued compared to execution, and shares his systematic approach to generating, testing, and deliberately trying to break his own ideas. The talk is rich with technical examples from VR development, computer graphics, and even rocket engineering.

---

## 1. Main Themes and Core Ideas

### The Myth of the Lone Inventor

Carmack directly challenges the cultural narrative of the genius inventor with a single brilliant idea:

> "We have in our culture the broader culture here this sense that everybody loves the idea of the lone inventor that has the brilliant idea that then they patent it, they get rich afterwards, or it's stolen by some faceless evil company and they're exploited."

He describes regularly receiving emails from people who believe they have a "magical idea" and want him to sign NDAs before revealing it. His assessment of these ideas is consistent:

> "Invariably within these cases we'll go through the stuff and it's either something that's obvious to someone that's kind of a part of the industry that they're talking about, or it's something that has a fatal flaw, or it's just kind of incoherent, or it doesn't really address things in different ways."

### Ideas vs. Execution

The central thesis of the talk is that execution dramatically outweighs the initial idea:

> "A good project is a result of hundreds and hundreds or even thousands of good decisions that are made along the way. You could start with a great idea and yet the implementation's not good, it's gonna fail. Good implementation is where you need to focus your efforts on because the ideas, they come and they go."

Carmack quotes Robert Heinlein: **"An idea is worth exactly one bottle of scotch."** He elaborates on a Heinlein story where the author gave a struggling writer friend "a whole page full of ideas" to help him get unstuck, illustrating that ideas are abundant for those who generate them consistently.

### The Psychological Value of Devaluing Ideas

Carmack presents what he calls a "cocktail party theory" - that deliberately ascribing low value to ideas may be a psychological hack that leads to having more of them:

> "Ascribing low value to ideas may be helpful in getting more ideas. I see a lot of these people that feel that they've gotten this idea and it's so valuable and they latch on to it... they won't necessarily look at it as critically as they might want to, as they probably should, or they will be jealously guarding of it."

This connects to avoiding what he calls "pet ideas" - ideas that become precious because they haven't been tested.

---

## 2. Key Insights About Software Engineering, Productivity, and Work Philosophy

### Ideas Come from Working in the Mud

> "You get the ideas by being down in the mud working on the problems. It's the hard work that leads you to the insights that are hopefully the great ideas."

Carmack emphasizes that research "is not about these lightbulb brilliant ideas that just strike you out of the blue but it's a whole lot of work that leads to the ideas."

### Farming Creativity

Carmack rejects the romantic vision of the genius staring at a blank wall waiting for inspiration:

> "I have this argument or this discussion lecture even with some creative people where I would have some designers that would be in kind of this funk about their not feeling inspired... I will be brashly telling them no, you can farm your creativity by just working through, exposing yourself to lots of things, always looking at them through the lens of the problem that you're working on."

He advocates for "trawling through all sorts of stimulus" while keeping your current problem in mind, rather than waiting passively for inspiration.

### The Joy of Breaking Your Own Ideas

One of Carmack's most distinctive insights is treating idea-busting as a pleasurable puzzle:

> "I ride the idea high at the beginning, I'm like oh this is a great idea, this has all these wonderful characteristics, but it's a little puzzle to figure out how to bust the idea."

He describes the satisfaction: "I can pat myself on the back when I break my own ideas. I'm very happy with showing clearly that this doesn't work."

### The Danger of Untested Ideas Becoming Pet Ideas

> "Ideas that I have that I don't try to engage and grapple with quickly, I find myself falling into more of a pet idea side of things... I wind up getting ideas and they sit there and they turn around in my head for a while and without testing them I get a little bit attached to them."

This is a warning about intellectual honesty - untested ideas can calcify into beliefs you defend rather than hypotheses you evaluate.

### Antifragile Approach to Ideas

Carmack explicitly references Nassim Taleb's concept of antifragility:

> "Your best system is one where you can take great gains from the highs, from the winning solutions, but you are not damaged much by the lows. That's the way I approach ideas now - I get the lightbulb or the little moment of enlightenment there and joy... but I am already kind of slightly smiling to myself, it's probably not gonna work out but it's sure fun while I'm having the idea."

### The 4x Rule

Throughout the talk, Carmack emphasizes that a 4x improvement is the threshold where things start to matter meaningfully:

> "4x is actually usually the number where things start mattering... a lot of computer speed stuff where 4x is when your computer got a whole lot faster."

---

## 3. Notable Stories, Examples, and Anecdotes

### The DMA Controller Story (Personal Early Failure)

Carmack shares a formative early experience with idea disappointment:

> "I can remember on the PC 80 thinking I could hijack the DMA controller to blitz screens and I'm like oh this will be great, this will be an enormous speed up, it'll be asynchronous and it'll be great, and I never could get it to work and I was bummed out for days afterwards."

### Palmer Luckey and Oculus

Carmack uses the founding of Oculus as a counter-example to the "idea guy" myth:

> "The reason Oculus is here today is because Palmer not had a bright idea but built a whole bunch of prototypes that eventually were physical artifacts that could make their way to my hands and could wind up building the things that kind of got us where we are here today."

### The "I Invented the Holodeck" Email

Just before the talk, Carmack received an email from someone claiming to have "invented the holodeck" and filed a patent:

> "Last week I got yet another one of those emails coming in from a young guy that said 'I've invented the holodeck, I have come up with this invention and I filed a patent for it' and he sent it to me and Michael Abrash and Palmer."

### Kent Beck's Introduction - The Stupid Trick

Kent Beck's introduction reveals a key Carmack lesson: spending two months on a perfectly clean implementation of tracer bullet sparks that couldn't be made performant, then solving it with "a stupid trick":

> "The lesson of that for me is that even if you're really really smart, sometimes the best way to be really really smart is to figure out why you don't have to be really really smart."

### Reading The Annotated Turing

Carmack describes getting excited while reading about mappings from the continuum to n-dimensional space, thinking it could apply to light fields:

> "I got hugely excited because there's all this stuff that I'm working on with light fields and some of these other areas that are these high dimensional spaces that are very sparse... unfortunately it was like oh I already knew that, this is kind of just the bit spreading trick."

Even the "failed" discovery reinforced his practice of constantly exposing himself to diverse material.

---

## 4. Technical Topics Covered

### VR Rendering and Foveated Rendering

Carmack discusses the challenge of achieving "retina class resolution" (16K x 16K displays):

> "The eye only has that resolution in a very very small area so called the fovea... instead of rendering the entire screen at a super high resolution you render the screen at a low resolution and then you render a smaller inset area at a higher resolution."

He describes pushing for the "multi-view extension" to render stereo views and foveal inserts efficiently.

### Projective Geometry for Variable Resolution Rendering

Carmack describes an idea for rendering with varying pixel density by using off-center projections:

> "If you have a single view that projects instead of projecting normal onto the surface, you're projecting kind of off centered there... that winds up giving you the direction of the compression of the angles going in the right directions."

This could achieve a "factor of four" improvement over conventional rendering.

### Light Fields and Luma Graphs

A detailed technical section on light field technology for VR panoramic capture:

> "The idea behind light fields is that if you had some bounding region around you and from each of these regions you had light rays coming off in all the different directions, you could in theory then synthesize any view inside here."

Carmack proposes a novel compression approach using dithered interleaved samples to potentially achieve 4x space savings.

### Depth-Correct Time Warping

> "We have this system that we apply to the virtual reality renders where you render your scene and then at the very last moment before we show it on the screen we sample the sensors again and we distort that scene in a way that lets it be closer to where you actually are."

### Drawing Order Optimization (Minecraft)

Carmack walks through his thought process on optimizing Minecraft's block rendering order, ultimately finding a counterexample that "busts" the idea:

> "You have blocks like this with a solid wall here, solid wall there... you have a sequence where from over here this one has to occlude this one, from there that one has to occlude that one, but from here this one has to occlude that one. So the idea is busted."

### Simulator Sickness Solutions

Detailed discussion of VR comfort, including:

- **The root cause:** "When your brain is seeing an image set that it accepts well enough and it's accelerating in some way that's different from what your vestibular system is telling you, that mismatch causes the discomfort."
- **Stutter turning:** Breaking angular rotation into 10Hz discrete steps
- **Lag and linearize:** Adding latency to convert parabolic motion into linear motion
- **Deterministic jump mapping:** The breakthrough solution for Minecraft

> "When you jump from here up to there is not this parabolic arc - I wanted this perfect linear arc that just takes you directly up there... this works magically."

### Rocket Engineering Ideas

Carmack discusses several aerospace ideas he hasn't had time to test:

**Spiral welding for rocket tanks:**
> "In a cylinder you've got twice as much stress going this way as you have going this way, and welding always impacts the strength of things... but if you spiral weld it then all of the welds are at a small angle."

**Gun barrel dynamics for rockets:**
> "The burning propellant here is not only pushing the payload but it's pushing the other propellant, so the propellant gets pushed and then it starts burning and you wind up being able to achieve in some cases a higher velocity than you can with a traditional rocket."

---

## 5. Career Advice and Lessons Learned

### Build Prototypes, Not Patents

> "If you're thinking about ideas, this may be the first time they felt that they had a really great idea... I tried to let them know that it's great to have ideas but you need to have lots of them because lots of your ideas won't work out very well, and the way to go about it is to try to build the things, try to build the prototypes."

### Have Many Ideas

> "You need to have a dozen more ideas before you land on something that really is great."

### Math Takes Time

Carmack offers encouragement to those intimidated by advanced mathematics:

> "A lot of the math, the heavy math in projective geometry... it took me a long time. There were many many years, a decade, when I was considered this graphics guru genius when I really couldn't do from scratch a lot of the mathematics that underpins a lot of that. But slowly, eventually, with a couple decades of experience, most of it did eventually sink in on me."

### The Value of Diverse Learning

> "I find myself more and more nowadays seeing this serendipity that seems almost weird in some ways, that I can be learning something in one place and then reading something completely unrelated and finding some reference to it or some tie between that."

---

## 6. Philosophical Approach to Engineering and Problem-Solving

### Ideas Revisited Over Decades

> "These thoughts go all the way back to the times of Quake thinking about draw order, and the fact that they can come up in topics that are happening today, 20-something years later, is interesting. There's something to be said there for ideas that even didn't pan out in the old days sometimes come back and can make an impact."

### Challenge Ideas Immediately

> "I feel good when I try to attack the idea early. Ideas that I have that I don't try to engage and grapple with quickly, I find myself falling into more of a pet idea side of things."

### Working From Outside In

Carmack describes his approach to testing ideas:

> "I start thinking through how would I build this, going kind of from the outside in, until eventually I started drawing the pictures of the blocks and figuring out what busts the idea."

### The Iterative Path to Good Solutions

The Minecraft comfort solution exemplifies his iterative approach:

1. First attempt: Stutter all accelerations to 10Hz - "terrible, completely jittering"
2. Second attempt: Lag and linearize - works reasonably but adds latency
3. Final solution: Recognize deterministic jump patterns and map them to linear paths - "works magically"

> "This came from three steps along the way where initial ideas and struggles working through, then the different things, and then winding up here with something."

---

## 7. Memorable Quotes and Striking Statements

On the value of ideas:
> **"An idea is worth exactly one bottle of scotch."** (quoting Robert Heinlein)

On the joy of idea generation:
> **"This is the best time to be doing what I'm doing - having a brilliant idea, thinking it's gonna be great. But I am already kind of slightly smiling to myself, it's probably not gonna work out but it's sure fun while I'm having the idea."**

On breaking your own ideas:
> **"I can pat myself on the back when I break my own ideas. I'm very happy with showing clearly that this doesn't work."**

On farming creativity:
> **"You can farm your creativity by just working through, exposing yourself to lots of things, always looking at them through the lens of the problem that you're working on."**

On where ideas come from:
> **"You get the ideas by being down in the mud working on the problems."**

On the romantic myth of genius:
> **"I think our culture somewhat inappropriately does give this vision of the genius that is just staring, doing the thought experiments, staring at a blank office wall, and that's how you get your enormous insights."**

On prototyping over patents:
> **"The reason Oculus is here today is because Palmer not had a bright idea but built a whole bunch of prototypes."**

Kent Beck on Carmack:
> **"Even if you're really really smart, sometimes the best way to be really really smart is to figure out why you don't have to be really really smart."**

On having more ideas than time:
> **"It's great when you wind up having more ideas than you get an opportunity to explore."**

---

## 8. Views on Code Quality, Optimization, and Craftsmanship

### The Obsessive Care Theme

Kent Beck frames the entire series around this theme:

> "One of the things I noticed in teaching engineers - young engineers don't seem to understand just how deeply really good engineers care about what they do... it borders on obsession and it's on the wrong side of the border, but that's where really extraordinary results come from."

### Pragmatism Over Purity

The "stupid trick" story from Kent's introduction exemplifies Carmack's pragmatism - two months spent on a clean implementation, abandoned for a hack that worked.

### Latency as a Currency

On VR comfort work:
> "Latency is something that I crusade against in almost all other cases. It's strange for me to be saying we're gonna add latency here, we're gonna spend latency to try to make it more comfortable."

This shows a sophisticated view of optimization - latency can be "spent" when it buys something more valuable.

### The 4x Threshold

Carmack repeatedly emphasizes that meaningful improvements require substantial gains:

> "4x is actually usually the number where things start mattering... 4x is when your computer got a whole lot faster."

This suggests a focus on high-impact optimizations rather than marginal improvements.

### Deep Technical Investigation

The level of detail in Carmack's technical examples demonstrates his approach - he doesn't just have high-level ideas, he works through the specific implementation details until he either validates or breaks the concept.

---

## Key Takeaways

1. **Ideas are cheap; execution is everything.** A successful project results from thousands of good decisions, not one brilliant insight.

2. **Deliberately try to break your own ideas.** Make it a game to find failure cases early, before you become attached.

3. **Creativity can be farmed.** Expose yourself to diverse stimuli while keeping your current problem in mind.

4. **Untested ideas become pet ideas.** The longer you hold an idea without testing it, the harder it is to evaluate objectively.

5. **Ideas compound over decades.** Insights from early work resurface in new contexts years later.

6. **4x improvements matter; marginal gains often don't.** Focus on substantial wins.

7. **Math takes time.** Even Carmack didn't fully understand the mathematics behind his graphics work for a decade.

8. **Build prototypes, not patents.** Physical artifacts and working code beat theoretical claims.

9. **The joy is in the process.** Enjoy having ideas AND enjoy breaking them - both are part of the work.

10. **Sometimes the stupid trick is the right answer.** Pragmatism over purity when it comes to shipping.

---

*This analysis is based on the transcript of John Carmack's talk at Facebook's inaugural "Deep Thoughts Engineering Speaker Series," hosted by Kent Beck.*
