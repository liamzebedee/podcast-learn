# John Carmack: Ideas and Engineering
## Facebook Deep Thoughts Engineering Speaker Series (Hosted by Kent Beck)

---

## Introduction by Kent Beck

Welcome to the inaugural Deep Thoughts Engineering Speaker Series. My name is Kent Beck. I help engineers educate themselves at Facebook in various ways.

Just a second about the series. One of the things I noticed in teaching engineers—I do a lot of one-on-one teaching—is young engineers don't seem to understand just how deeply really good engineers care about what they do. So the theme of the series is to bring people who really care about their work to talk about what they really care about the most. It's been a theme in my career. I mean, it borders on obsession, and it's on the wrong side of the border, but that's where really extraordinary results come from.

So the first lesson for me in setting up this series was: **ask for exactly what you want**—you can compromise later. I thought, well, okay, if we want to get the best engineers at Facebook to talk, who's number one on that list? It's Carmack. Like, it's not even a question. And so I just emailed him and he said yes. Go figure. Sometimes not having a sense of shame is a problem, but sometimes it comes in handy. So thank you very much for making the trek up from the wilds of Dallas to meet us.

I always like introductions that are short—and this will be fairly short—but I also like introductions that are personal. The lesson that I learned from John is: I saw a post that you made at one point where you described spending two months working on the perfect implementation of something—I'm gonna forget the details—sparks flying off a tracer bullet or something like that. There was a really good way to implement that that was perfectly clean, and you just couldn't get a performant implementation of it. So you just said, *"Well, but there's this stupid trick, so let me just do this stupid trick,"* and it worked just fine, looked just fine.

So the lesson of that for me is that even if you're really, really smart, sometimes the best way to be really, really smart is to **figure out why you don't have to be really, really smart**. I want to thank you for that lesson. I've tried to keep that in mind for the rest of my career.

---

## The Value of Ideas in Engineering

I got the invitation and I do kind of beat myself up for not being more engaged with the broader Facebook engineering community here. I do kind of like my little hermitage down in Dallas, but there's more that I should be doing to try to be a part of the community here.

I thought about it and I wrote down at least a dozen things that I could go and talk for hours about that would be interesting topics, hopefully educational to some degree. But what I settled on, somewhat topically, was this notion of **ideas and engineering**.

This was kind of triggered by before Oculus Connect. Michael Abrash had sent me an email asking if it was okay to tell one of the stories of the original Quake development—about how I had gone through all of these different paths for basically visibility culling to get the speed up to a certain way before settling on this one **potentially visible set** (PVS) method. He did a nice presentation at Connect with the basic idea being that **research is not about these lightbulb brilliant ideas that just strike you out of the blue, but it's a whole lot of work that leads to the ideas**.

I quibbled a little bit and said that there definitely are lightbulb ideas where you can be sitting there working and something does come to you in a flash—that may or may not be a great idea. But the core of the lesson is absolutely true: **you get the ideas by being down in the mud working on the problems**. It's the hard work that leads you to the insights that are hopefully the great ideas.

## The Myth of the Lone Inventor

We have in our culture—the broader culture here—this sense that everybody loves the idea of the **lone inventor** that has the brilliant idea, that they patent it, they get rich afterwards, or it's stolen by some faceless evil company and they're exploited. These memes run through our culture in different ways.

Over the years, as someone with a little bit of notoriety as a game developer or a rocket scientist or whatever, I get emails from a lot of people that are often earnest people that believe that they've gotten a magical idea. Usually it's approached by saying, *"I've got a great idea. I need you to sign an NDA so I can tell you my great idea, and then maybe you can work on it with me."* They're usually people that think, *"Okay, this idea is magical. I can't build it, but we need to find somebody that can implement this idea, and then we'll all be hugely successful."*

Sometimes I can talk these people down from their patent application and their NDA requests, and I can look over the stuff. I give advice for free—I'm happy to hear your ideas and tell you what I think about them. And invariably, in these cases, we'll go through the stuff and it's either something that's obvious to someone that's part of the industry they're talking about, or it's something that has a fatal flaw, or it's just kind of incoherent, or it doesn't really address things in different ways.

But I still try to encourage most of these people. If you're thinking about ideas, this may be the first time they felt that they had a really great idea—often they're young, not always. I try to let them know that **it's great to have ideas, but you need to have lots of them**, because lots of your ideas won't work out very well. And the way to go about it, of course, is to try to build the things, try to build the prototypes. Often it means really knocking your ideas down—it turns out that your great idea is probably not that great. You may need to have a dozen more ideas before you land on something that really is great.

## Ideas Are Cheap, Execution Is Everything

There's a quote by **Robert Heinlein**, the science fiction author, and he said that *"an idea is worth exactly one bottle of scotch."* For a writer—someone who even more than software in many cases, ideas are the stuff that they build—it's still a matter of **execution being much more important than that original core idea**.

There was another Heinlein story about how one of his friends, a struggling writer, was really down, and Heinlein just handed over a whole page full of ideas—wonderful ideas that could each be turned into some great science fiction story—with, *"We hope that this gets you unstuck, that you can follow something off from this."*

I've taken that tack through most of my career: trying to say that the ideas really aren't the important thing—**it's the execution**. A good project is a result of **hundreds and hundreds or even thousands of good decisions** that are made along the way. You could start with a great idea and yet, if the implementation's not good, it's gonna fail. Good implementation is where you need to focus your efforts on, because the ideas—they come and they go, and it hasn't mattered that much.

This influences in many ways my views on **software patents** in some of these other areas, where I don't think that trying to nail down this high value on a specific idea—when the idea is this tiny fraction of the product—is a particularly good thing.

## When Ideas Do Matter

But still, there's this sense that clearly ideas mean something. There's plenty of cases where you have competently executed projects that failed to leave any dent on the world, even though they were done with all the right decisions. But there was something missing there—maybe those grand ideas were necessary to make the big impacts.

I've actually been toying with this idea about ideas recently—what you could call a **cocktail party theory**, something that you wouldn't necessarily defend to the death but it's worth thinking about a little bit. And that's that **ascribing low value to ideas may be helpful in getting more ideas**.

I see a lot of these people that feel that they've gotten this idea and it's so valuable, and they latch on to it. They think that this is something that's going to be great. They won't necessarily look at it as critically as they might want to, as they probably should. Or they will be jealously guarding of it—different behaviors that I see in other people. And in fact, I've seen in my earlier days: I can remember having early ideas when I was at the age of many of these people that email me.

I was on the PC AT thinking I could hijack the DMA controller to blitz screens, and I'm like, *"Oh, this will be great! This will be an enormous speedup, it'll be asynchronous, and it'll be great."* And I never could get it to work. I was bummed out for days afterwards—this brilliant idea that I was all hyped up on just wasn't gonna work out.

## Busting Your Own Ideas

I had a timely thing about this. I had already decided on this topic a few weeks ago, and last week I got yet another one of those emails coming in from a young guy that said, *"I've invented the holodeck. I've come up with this invention and I filed a patent for it."* He sent it to me and Michael Abrash and Palmer. Palmer is probably getting a lot of these things now also.

I had to tell him, *"Well, first of all, I'm sorry but I can't read your patent application."* But I try to be encouraging still. I tried to say, *"Alright, well, you need to start prototyping things."* I should mention that **the reason Oculus is here today is because Palmer not only had a bright idea, but built a whole bunch of prototypes** that eventually were physical artifacts that could make their way to my hands and could wind up building the things that kind of got us where we are here today.

So this sense that the idea wasn't the important thing, but iterating on it, building it over and over. I've been thinking kind of through that lens though: am I ascribing perhaps too little value to some of these things, but doing it as a **psychological hack** where I'm tricking myself into not wasting time or spending time in ways that are not going to be as productive? If I just say, *"Well, ideas come, ideas go..."*

I mentioned to Michael Abrash about my original comments, and I sent a couple more emails: *"Here's the idea that I had this week, here's the idea that I had right now."* And now I look at them and say, *"Well, this is kind of interesting. This would be awesome if it works out, but it probably won't."*

I almost look at these things now—I've been through the idea train enough times—where you look at something and think, *"Wow, this will be glorious if it works."* And I get the idea high at the beginning, but I've done it enough times now. You can say, *"Well, it probably won't."* And it can almost be the **puzzle game** then to find out how to bust my own idea.

## A Case Study: Minecraft Block Ordering

For instance, just a couple weeks ago, I was discussing with the Microsoft Mojang developers about Minecraft—ways to optimize Minecraft for VR and different things. This kind of tiny little topic came up where this is a very, very small idea. I'm thinking that, okay, if we optimize—everything's broken up into all of these blocks, the world has chunks and they're rendered, they're sorted in the order that you render them—but maybe there would be a way that we could optimize the ordering of the indexes that make up all of these individual blocks so that we could guarantee a certain draw order irrespective of where you're at.

This would be a minor benefit. It would make certain scenes go a few percent faster. I started thinking about it—there are some classic cases with occlusion. And what's interesting is these thoughts go all the way back to the times of Quake, thinking about **draw order**. And the fact that they can come up in topics that are happening today, 20-something years later, is interesting. There's something to be said there for ideas that even didn't pan out in the old days sometimes come back and can make an impact. Reality is like that.

One of the classic issues with computer graphics is drawing order—either you're drawing **back-to-front in painter's order**, or nowadays on modern hardware you're trying to draw **front-to-back** so that you don't wind up drawing things once you've already filled them in.

In some cases for simple geometries, there are orders statically that you can assign to things. If you had a surface with back-face culling, you could say that if you wanted to draw front-to-back, you could always draw certain faces first because nothing can ever occlude those—they would be the topmost thing. Then you would have to draw the middle ones, and at the final part you could draw the rest.

But there are lots of surfaces, lots of orders of geometry that don't work out like that. You can make a set of three things that overlap in a way where there's no static order that you can draw the triangles in that will guarantee that they get drawn in the right order. You have to introduce splits.

So being aware of both of these cases, I was at least thinking, *"Okay, well, Minecraft has this interesting characteristic that everything is diced into blocks—it's all just cubes. Is it possible to apply a static ordering since you know that nothing would ever have to be split like this, because they can't cross over? Would it be possible to make a static ordering?"*

This is one of those things—this would be clever. It would be no additional memory. It would give us some speedup in some of the worst cases when you have lots of occlusion. And I'm thinking, *"Oh, this is a great idea. Aren't I clever? This will be fun."* And I can start thinking about the implementation.

But I look at it like, okay—I start thinking through how would I build this, going kind of from the outside in, until eventually I started drawing the pictures of the blocks and figuring out **what busts the idea**. You have blocks with a solid wall here, solid wall there, a little wall there. You have a sequence where from one angle, one block has to occlude another, but from another angle, a different block has to occlude the first one. So the idea is busted—it doesn't actually work out. Seemed like a great idea, but there's a clear failure case and it doesn't work.

This is just the type of little idea where I ride the idea high at the beginning—*"Oh, this is a great idea, this has all these wonderful characteristics"*—but it's a little puzzle to figure out how to bust the idea.

## Antifragile Thinking

The author **Nassim Taleb** wrote *The Black Swan*, *Fooled by Randomness*, and his more recent one was *Antifragile*. He espouses a kind of interesting theory that I recognize from the way I look at a lot of things. The idea is that **your best system is one where you can take great gains from the highs, from the winning solutions, but you are not damaged much by the lows**.

And that's the way I approach ideas now. I get an idea, I get the lightbulb, or the little moment of enlightenment—*"This is great! This is like the best time to be doing what I'm doing, having a brilliant idea, thinking it's gonna be great."* But I am already kind of slightly smiling to myself: *"It's probably not gonna work out, but it's sure fun while I'm having the idea."*

And then **hunting the way that it winds up not working out** becomes an effective challenge. That's the best use of the time. If you're not trying to bust your own idea, you swerve away from the things that may wind up punching holes in it. I mean, you see this in all sorts of things about how people, when they're invested and attached to certain ideas, will look at the things where it looks like the ideas working out, but not so much on the things that may punch holes in it or challenge it in different ways.

So now I try to look at these things like: **get the joy out of it, but then really try hard to punch holes in my own idea**. And that becomes almost an enjoyable task. And I can pat myself on the back when I break my own ideas. I'm very happy with showing clearly that this doesn't work.

## Farming Your Creativity

These wind up coming from—I could trace even the broken ideas—the depths of these things that went back to graphics work 25 years ago. And that's down to again the part about being down there in the mud working with the idea. That's how you get these moments of enlightenment—it's working through, farming the ideas and the things that go into it.

I have this argument or discussion—lecture even—with some creative people, where I would have some designers that I would talk with that would be in this funk about not feeling inspired, not getting their creative spark that they're looking for, their muse isn't with them in some way. And I will brashly tell them: **"No, you can farm your creativity by just working through, exposing yourself to lots of things, always looking at them through the lens of the problem that you're working on, and plowing through."**

Not staring at a blank wall—which I think our culture somewhat inappropriately does give this vision of the genius that is just sitting there doing the thought experiments, staring at a blank office wall, and that's how you get your enormous insights. And while some of that does happen—works for Einstein in some ways—I think that **it's far more productive to be just trawling through all sorts of stimulus** for the different things that you're looking on, looking at it through the lens of your current problem.

Sometimes it pays off. I was recently reading the book *The Annotated Turing*—it's Charles Petzold's book on going through Turing's old papers. There was talk about how there's a mapping from the continuum to all points in an n-dimensional space, and I got hugely excited because there's all this stuff that I'm working on or interested in with **light fields** and some of these other areas that are these high-dimensional spaces that are very sparse. Like, *"Oh, some new mapping for this would be a wonderful thing! This would be great!"*

Once I deciphered the mathematical language, unfortunately it was like, *"Oh, I already knew that."* This is kind of just the **bit-spreading trick** where if you have a sequence of bits going off in some way, you can just turn that into a two-dimensional space by taking like every second bit and making coordinates out of it. You could do that for any n-dimensional space—you can spread them out. But still, it was one of those things where I was reading a book completely unrelated to anything that I was working on, and if I hadn't already known that, that would have been a good insight. That's something that's useful for a lot of cache-blocking things and different stuff like that.

But that sense of being out there—not so much searching specifically for something, but **continuously exposing myself to all of these other things** and seeing what the current problem that I'm looking at applies to—I find myself more and more nowadays seeing this serendipity that seems almost weird in some ways, that I can be learning something in one place and then reading something completely unrelated and finding some reference to it or some tie between that.

## High-Resolution VR Rendering: A Promising Idea

One of the significant problems with virtual reality—and this was the first idea that I forwarded to Michael right after he had sent me the original email—one of the things that you've probably heard people talk about in VR is that we need **16K by 16K displays** to really get retina-class resolution for VR. And historically you look at that and say, clearly, while we could actually build that with wafer-scale integration of silicon micro-displays, that would be an interesting thing. We couldn't render that in any reasonable system today. And really that's not the direction that things will eventually get.

It's not nearly as bad as that seems because **the eye only has that resolution in a very, very small area called the fovea**. Several of us have done research and prototyping where instead of rendering the entire screen at a super high resolution, you render the screen at a low resolution and then you render a smaller inset area at a higher resolution.

This works and is useful even on our systems today because our optics are not great across the entire field of view—they're clearest in the center and blurrier as you go out. So there's some argument that doing this sort of rendering today is a good idea. This is one of the reasons we've been pushing for the **multi-view extension**, which is a way for us to push all the draw calls for a scene down and then have the driver and the hardware reissue those to make a second stereo eye view, and ideally a second foveal inset, and another foveal inset for the other eye.

The magic screen that we want—and there's work being done on this now—would be something that could track your eye and then move this region around to exactly where it needed to go. That would be something where you could deliver hopefully this retina-class resolution by having that in only this tiny little area. No screen like that exists now, but we have people that are working on technology that may get us this maybe sooner rather than later.

So there's still the question of how you wind up delivering all those bits to it and rendering it. A few of us have built systems like this where you render kind of two separate views. But we talk about the fovea as if it's this fixed little region—*"Here's the fovea region of your eye and it occupies this many degrees of arc"*—but it's really not like that at all. If you look at the Wikipedia graph for it, you wind up having something that looks like lots of resolution right in the center and then a smooth curve going down, with one little gap where you've got your blind spot where the optic nerve goes in.

Looking at this, it occurs to me: the shape of that curve—that looks a little bit like a **projective texture mapping curve**. Like you've got a divide in there somewhere. I started thinking about this again where if you had this two-step thing, you're looking at saying we have one image at this resolution and then one image at that resolution, and you can take the integral of the difference between there to see how non-optimal that would be for what you're trying to do. It's still a whole lot better than picking one average sort of across the whole thing, especially if you want to get a lot in there, but it's not really what you'd like to have.

So I start thinking about how else could we address to build some rendering like this. One of the tragic things about the conventional graphics pipeline is the wider you make the field of view, the worse it puts the pixels. If you have a field of view something like 80 degrees or so, each pixel is not too far off between the angular resolution as it goes from center to edge. But the wider you make it, the worse it gets. If you render 120-degree field of view, the pixels over at the edge actually have much more resolution on the outside—which is exactly where we don't want it. It's doing the inverse of what we'd like to have.

Which is what pushes us to saying, *"Well, we'll do the whole broad thing at some low resolution and then we'll do a tighter inset."* But I started thinking that **projective geometry** might be able to help us with this.

A lot of the math—the heavy math in projective geometry and a lot of the higher math—it took me a long time. There were many, many years, a decade, when I was considered this graphics guru genius when I really couldn't do from scratch a lot of the mathematics that underpins a lot of that. But slowly, eventually, with a couple decades of experience, most of it did eventually sink in on me to be able to formulate some of these things more directly.

What I started thinking about was: what if you have a single view that projects, instead of projecting normal onto the surface, projecting kind of off-centered there? You could think about this like you had the whole screen but you're only taking the end of it where it's stretching out in the wrong direction—taking it and making it the right direction, and then doing the entire thing. So you're looking down sort of at the corner of something. It would be rendering once that way and once that way. That winds up giving you the direction of the compression of the angles going in the right directions—it's taking what's doing the opposite of what we want, turning it around and making it do what we want.

That winds up getting something that curves up, gives you an increasing curve—not an enormous difference, maybe a factor of two off from what you'd like to have. But this makes it a factor of two in the right direction, which makes it a **factor of four** better than what we would have from our conventional rendering. And a factor of four is nothing to sneeze at.

I started taking the steps to try to bust it—I wrote some code, made some checkerboards, rendered the images. It looked really pretty promising. Looking at the corner of a cube, I got tripped up a little bit because the three-dimensional aspect of this is not the same as the two-dimensional. But still it looks pretty good. Stretching it out starts to show some issues where the pixels get very distended, and there's a degree of anisotropy where the core center of it where your fovea would be looking is extremely high pixel density—could get up to very much what you'd like to see—but on the outside you've got these very stretched-out pixels. I don't know whether that's good or bad or a problem or not. That's something that might not be a problem because that's inherently what you're not looking at—that's something that's only happening at the edges, if they're well-filtered.

Maybe that's a good enough idea. But even if it only works out where you don't extend it—you just leave it at the cube—there are some GPUs that have hardware support already for distributing primitives across cube faces, mostly for rendering environment maps. So if you say, *"We're gonna take the three sides of a cube here and we're going to push one stream down it, it can split them all up."* That seems almost optimal. Maybe that's only a factor of four better than what we're doing now, but **factor of four is a pretty wonderful thing in a lot of cases**.

So this is an idea which I'm at least cautious about—maybe a great idea, this may be something that has some real significant win to it.

## The Danger of Pet Ideas

I noticed that I feel good when I try to attack the idea early. I see this where ideas that I have that I don't try to engage and grapple with quickly—I find myself falling into more of a **pet idea** side of things.

I have this problem a lot now. I'm not actively building rockets, but I still think about aerospace stuff. I still think about all this stuff when I'm trying to go to sleep some night, having rocket systems dreams or whatever. But that's problematic because I don't have the shop running where I can go and build and test those things right now. So I wind up getting ideas and they sit there and they turn around in my head for a while. And without testing them, I get a little bit attached to them—they're like my pet ideas in some ways. And I think that I fall into some of the same traps that the people that wind up emailing me about things fall into.

For instance, every time I look up at ductwork I see **spiral-welded ductwork**. This is done by taking a strip of metal and, instead of forming it into a cylinder and welding it in different ways, you have a machine that winds it and makes a continuous weld. Now that's an exciting thing from a rocket engineering standpoint because normally when you make a cylinder—if it's a long cylinder—you've got welds going around and then you have one weld that goes down the side.

The problem is that in a cylinder, you've got **twice as much stress going circumferentially as you have going longitudinally**, and welding always impacts the strength of things. So you have a supercritical weld going down there. You get companies like SpaceX that do very nice **friction-stir welding** to try to make the best possible things. But if you spiral-weld it, then all of the welds are at a small angle, which is—you've got twice as much strength going that way, so even if the weld de-rates by 40 percent, you still have a really good solution. And plus it's really cheap, which is why they make ducts out of those.

So I wind up thinking about all these ideas about how we should just take some maraging steel and roll this through—I get that worked out—and then you've got a great system that can be built inexpensively, or perhaps even on-site. You can build enormous things like this. Maybe you can spiral-weld a Saturn V tank on-site where you're going to launch it, or on a barge, or whatever you need to do. Maybe it's even possible to gently adjust the angles to make tapers, to be able to make actual cone sections from there, to make a one-piece monopropellant-based launch vehicle tank.

And this is an idea that I've actually been kicking around for a while, and I'm probably gonna be years before I wind up getting around to testing this. So that's not as valuable of an idea in many cases because I haven't been able to test it. I probably have a fondness for this idea, and I get reminded of it every time I wind up looking at exposed infrastructure.

## Rocket Engine Dynamics

Then there's other things, like the way a rocket engine works. You have a combustion chamber, you make hot gas up here and it expands, accelerates, and converts the thermal energy into kinetic energy coming out. There's all these issues about how you want a large expansion to accelerate it, but you can't do that inside the atmosphere.

An unrelated thing came up. I read some statistics about **muzzle velocities of battleship guns**, and there's an interesting aspect about that where they can fire at several times the speed of sound, even though the charge that's firing the shell is less than half of the full munition weight. You run the numbers from the traditional rocket equation and they're going faster than they should be if it was a rocket with that amount of propellant at that ISP.

And it's for an interesting reason. When you have a gun, you have a whole bunch of propellant in there. With a rocket engine, propellant comes in and it turns into gas kind of immediately—it comes in, turns into gas, it combusts and accelerates. With the gun, you wind up having something where it starts burning, but instead of burning at the end—like if you flipped a shell around and lit the end of it, it would be a gas generator rather like a rocket—but if you're actually pushing it out, the interesting thing is that the burning propellant here is not only pushing the payload, but **it's pushing the other propellant**. So the propellant gets pushed and then it starts burning, and you wind up being able to achieve in some cases a higher velocity than you can with a traditional rocket.

So I spend time thinking about, *"Well, how can we make a rocket engine that might have gun-barrel-type dynamics?"* And I've got sort of a test plan in mind, but it'll be years before I wind up getting around to spinning something up to try this.

## Light Fields: Compressing High-Dimensional Data

But then there are ideas that are at this middle ground, where **light fields** are an interesting technology. This is again something from recent months.

We have in virtual reality panoramic videos, panoramic photos. You can take two kinds that we have right now in production: **monoscopic panoramic photos**, where you basically sample the environment around you as if theoretically it was from a single point source. Realistically, there are multiple lenses and they have to deal with stitching and warping things around, but it's a sampling of the environment from one source. And those are easy to make fairly reliably, but you don't have any ability to have depth perception between your eyes or to move around at all.

The next step up from that are the **stereo panoramas** and videos, which are an enormous hack. They deliver value for us right now, but it's really a mess how they're defined and how they're created. That takes lots more cameras that are somewhat offset rather than all focusing into the center, and you stitch together something that looks kind of right for your two eyes and can deliver stereo when you're looking at things. But the things further away from the center aren't right till you look over at them. It's an intermediate step.

But where we all really want to be going is something close to **light field technology**. The idea behind light fields is that if you have—like our normal systems here—just rays coming off from one point sampling an environment around you, if instead you had some bounding region around you and from each of these regions you had light rays coming off in all the different directions, you could in theory then synthesize any view inside there. So you could say, *"Well, I'm gonna view up here, I want to make a view this way, I'll take some of the rays from here and some of the rays from there."*

And this actually works. You can have, if you have enough rays to be able to build this stuff from, you can **synthesize moving around in an area**. And that's pretty magical. I think that this is what we want from our VR snapshots—where you can duck down, you could look around a corner, you can get all of this.

But a raw light field takes an enormous amount of data—gigs and gigs and gigs of data. You're trading off resolution at all times because in the extreme case, you want to have what winds up being one rendering for every millimeter. You could take the box that you want to view in, and in the most raw case you want to step every millimeter or two across there and make thousands and thousands of renders at the full resolution that you want to be using.

This is interesting for demos. There are some things that have been done in these relatively blurry images. The step that people take generally to start making this more practical is to not just have rays with directions, but include **depth**. So you've taken an image here and you've got a picture, but you've also got a depth for it. And that lets you do much smarter things as far as saying, *"Well, I want to sample a ray here, I'm gonna hit it at that depth,"* and you can say, *"Well, that's not exactly the one that I want, I probably want something over here."*

In the simplest case, if you were inside a beach ball, then you could have one panoramic photo with one depth, and if it didn't have surfaces that changed a lot in their view as you moved around, that would be all the information you needed. But in most cases, we have occlusion—if I'm here, I need to be able to know what's behind that occlusion over there. So you have surfaces, you have views that are rendered from more points of view.

The depths are tricky to get. If it's synthetic, if it's just a ray-traced image, then you've got the information immediately. But if it's a real-world capture, then you start having to apply these computer vision and computational photography things to take your multiple cameras, extract depths from them, add them to your structure here so that you can start re-rendering them.

But they still take an enormous amount of data. You still wind up—if you want to have significant occlusion and complex structure there—you may need dozens of images at these full resolutions that you want, that wind up being spheres or hemicubes or something, along all these things. To the point where it's still stressful on even modern high-end systems.

So the idea that I started thinking about on this—and this came as a result of getting OTOY's demos, talking with them about their stuff, and then I toss the ideas back their way, see what everybody thinks about it—the trick when you do a projection from here: if you have an image and say it's got a room and you've got some object inside there, so you've got big depth discontinuities. When you wind up sampling a point on there from a ray that's not exactly where this camera came from, you have to wind up making an adjustment to the sample position, because you could say this would be exactly the right point if you were exactly at this camera point. If you're offset from this, then the point's actually going to be over here a little bit, and you can make a calculation based on the depth.

Interestingly, this is exactly the same system for doing what we call **depth-correct asynchronous** or **depth-correct time warping**, where we have this system that we apply to the virtual reality renders where you render your scene and then at the very last moment before we show it on the screen, we sample the sensors again and we distort that scene in a way that lets it be closer to where you actually are rather than where you were when you started on it. Normally we only do this for attitude, which is a simple projection, but if you have all the depth you can do this reprojection so that even if you're moving side-to-side you can have it do some of this stuff. You'll wind up with problems at the silhouette edges, but it's interesting that this is a technique that I had been working on years ago just for the time-warp reprojection, but it's also directly applicable for all of these light fields.

One of the problems with that is that if you start and you hit this point on the depth, if it actually says, *"Well, you should be over here,"*—if that's on the same surface, then that's really a good approximation. But if it's moved off of that surface and it's on something different, then that's actually going to be pretty wrong. If you look closely at a lot of the light field renderings—technically we should call these **lumigraphs** if they've got depth-augmented information with them, but there's a lot of confusion about terminology and everybody's making a "light-field camera" now if they've got more than one lens, that's just the buzzword—you'll see that in general these things look remarkably good when you have surfaces without a lot of occlusion. You can look at it and it can be great, you can duck down, move around, look at it from different angles and see changes in specular highlights and everything. But there are usually problems there at the edges of things. Like if we had one light field here, as I'm looking around that occluder there, there would be issues where you would see ghosts and double images and some of these other artifacts.

So my thinking for this is that if you just sample from—you've got a grid of light field images here and you can sample between the four of them—you've got the four closest images and then you can find the four closest rays on each of those, and you can just do straight filtering through all of those. But you wind up with ghost images.

My first thought on this was, *"Well, we can actually tell from the initial point and then the final point—we've got a depth from that—we can tell whether that was close or wildly off for what we were initially looking for."* So instead of just blindly blending all of those samples back together, we should go ahead and look at them and **throw out the ones that have clearly gone to another surface**. So you wind up just sampling from the ones that are the closest there to get rid of most of the ghosting.

But then as I started thinking about the samples that we're looking at here—you're in between four samples there, and you've got four samples that the ray's gonna be between—there's gonna be sixteen samples at your disposal. But what you really want to do is **find three of them that bound the sample that you want**, where you want to be able to say, *"I have a sample from here, a sample from here, a sample from here, and then here's where I am,"* and just do the interpolation between those. Because you may have other samples that are out here and then some of them that are way over here because they actually went to the wrong surface.

If you can identify the samples there, there's an interesting idea that occurred to me: we may be able to **save three-quarters of our pixel samples here** by saying that we have the four images that are the nearest ones for what we're doing here. They're all slightly different, similar images, very close. You look at that—there's an enormous amount of waste where it looks like the same wall on each of these. It is slightly different—they're slightly different positions so they have slightly different rendering artifacts—but there's a lot of commonality.

Now, these compress quite well. What you wind up doing if you want to compress these for transport is you wind up saying you have 64 images or something, you wind a spiral out, video-encode it, because it does very much look like these linear moves moving around and it encodes quite well. But you need them all decompressed to actually render them.

So the idea that I'm excited about that I have not yet proven or disproven is that if instead of making these from exactly the same central render points, if we offset them by a pixel each way so that you have a **dither interleave of the samples**—so if you had one, it might have samples from those angles, and then the next one over exaggerated scale might have samples from that angle, so that they're sampling different sets of angles. Now that would mean that the image there would be aliased—you couldn't sample it directly because it's stepping over information that you would need for direct referencing. But if you gather the potentially 16 samples—and it may only need to be done with potentially four samples even—you gather the samples from those different ones, throw out the ones that have off-kilter depth values, and then you find which ones bound the surface there... I think that that can be done where you can get a **4x space savings**.

And again, for 4x—4x is actually usually the number where things start mattering. I mentioned that on the resolution side of things. I used to say that about a lot of computer speed stuff, where 4x is when your computer got a whole lot faster—that would be a great thing.

I need to find the time to go and test this. It's great when you wind up having more ideas than you get an opportunity to explore. So of course I send some of these things over to OTOY and I hope they get to go explore them because I'm happy if it just works out. And it's possible that this could even be extended more ways. Where if you can tile by—if you can interleave on a 2x2 factor, maybe you can interleave on a 3x3 or a 4x4 factor. Maybe there's a **16x factor** that you could get. That would mean more sampling, it would trade a more expensive fragment shader to go and gather all of these and discard them and do those tests there, but it's a potentially larger impact. If you go too far, you wind up getting to the point where some of the changes in visual effects from different angles that you want to get from things like light fields you might not get, because you would have something all the way over here contributing samples that go over to it. But I'm suspecting it may be good for at least this kind of factor of four, which is exciting, and maybe it's good for even more.

## Solving Simulator Sickness in Minecraft

Another path of an idea in the last month that has actually been working out extremely well is again on the Minecraft project. One of the things that we've learned in virtual reality is the **simulator sickness** that most people associate with VR.

There's a lot of different types of discomfort that are issues in VR—there's eye strain from focus, eye strain from convergence mismatch—but what most people associate with is the kind of sick-to-your-stomach queasy feeling of simulator sickness. This is mostly a matter of when your brain is seeing an image set that it accepts well enough and it's accelerating in some way that's different from what your **vestibular system** is telling you. That mismatch causes the discomfort.

If you've got something curving up on a roller coaster in virtual reality but your body's staying still, your body is saying, *"My eyes and my vestibular system are not matching. You probably ate poison—you should throw up."* That's the kind of general theory behind a lot of this.

So in VR, the thing to avoid is **acceleration**. If you assume that your user is seated or standing roughly in place, anytime you're accelerating, that's when the body is going to complain. Linear motions are generally not a problem—you can be moving along, rocketing along even at speed in a straight direction, and if there's not too much stuff cluttering up your view, that's usually not a problem. But if you slowly accelerate up to a specific point—like certain space game launchers that rocket you down an area—that's particularly bad news. And some people are like, *"I close my eyes for that point because it's going to be uncomfortable."*

Now there's an interesting aspect about this where if you make changes in **discrete enough chunks**, then it winds up not being uncomfortable. One of the obvious things that especially affects the PC side of virtual reality is when you're turning. That's an angular acceleration—you may be staying motionless, but the angular acceleration is really bad news. Even people that are far less prone to simulator sickness than most people—and my theory about that is because I wear multifocal glasses, so the world is always swimming a little bit, so it's trained me to be better at virtual reality—but even there, just sitting and spinning, **stick turning** I call it, where you're going based on a continuous input, is pretty bad. And you don't want to do that for very long, and some people will be almost instantly sick from it.

But it's been found that if you break that up and you only do it at, say, ten Hertz—where it's no longer smooth, so it's this choppy stutter turn—it winds up not being uncomfortable. Now it doesn't look great because it's stuttering that way, but people can functionally play through things and wind up not being sick. There's an interesting trade-off there because it definitely gets you out of that sense of your brain being like, *"I'm buying this, this is great, I'm in this virtual reality"*—but *stutter stutter stutter*, *"Okay, I didn't quite buy that, but at least I'm not sick."* It's a trade-off that you can make, but it's always better to try to remove the accelerations as much as possible.

I advocate for my Gear VR playing in a **swivel chair** because you can just turn around like that wherever you want, and that's the worst offender kind of solved in a more direct way.

But Minecraft is one of these games that is almost the **worst possible case for simulator sickness** because not only is it rotating around as a major part of it, but it's bounding up and down. **Parabolic arcs are not your friend in virtual reality**, which is a shame. One of our very best games is a jetpack game, Omega Agent, and a lot of people really can't play it because it's lots of arcing around like that, even with some remediating steps that they've taken.

So trying to address the issues in Minecraft has been an interesting challenge. Obviously, I say, *"Well, just don't turn with a stick—turn in reality whenever you can. And if you need to turn with the stick, well, we can do the stutter turning, that's been proven out in a few different places, and that largely works."*

But there's all of these other little things in there—the bounding up, it's so much about hopping up blocks, falling down blocks—and that's just bad. It's all of these linear accelerations, and there's all these little things with minecarts and other stuff that do pull you around. And even starting and stopping—I've tried to argue that games should have instantaneous start, none of this accelerate up and friction ramp down. But when it's a game that you can play multiplayer, you don't want the VR people behaving in a different way, and that becomes a sensitive issue especially when it winds up being competitive.

So the idea occurred to me: well, what if we know stuttering basically solves the comfort problem? **What if I just identified any of the accelerations that are going to cause a problem**—whether it's a slow start, a friction stop, a minecart turn, or falling off—and I just stuttered it to ten Hertz? This would be like, *"Okay, we've identified the root of the problem and here's a solution for it."* Maybe this solves everything. Implement it—and it's terrible. It's completely jittering all the time. It just looks... it doesn't make people sick, but it's not fun to play because it's jerking all the time. It doesn't feel good, doesn't feel polished.

So it's kind of like, well, there's something to that thing about identifying all these things that could cause accelerations, and maybe there's a better way to approach it.

What I came to after that as the idea is: okay, I'm logging the information. Say you've got a path that goes up like this, and if you smoothly go through that, that's a set of accelerations—it's going to be uncomfortable. But if you were able to go ahead and **linearize that**—you just made it a linear ramp from there to there—that's no longer uncomfortable. There's one impulsive change to another slope and another impulsive change when you get off of it.

So I logged the positions, positions and velocities. It builds off of the work that I was doing with the stutter elimination, and I kept a little bit of a backlog. I called it **"lag and linearize"** where it lags it a few frames back and then turns it into linear steps. And it would do a few kind of smarter things about identifying exactly when you made a transition to jumping up or falling off—it could push it there.

This worked reasonably well. There was a tunable parameter where you could say—at the start, Minecraft works on 20 Hertz tick, so everything went in multiples of that. If you double that and said, *"Okay, now it's essentially a ten Hertz linear step,"* but everything gets interpolated between that, that helps a little bit. Then you go to three or four steps and then it's clearly doing this linearization thing. The jumps start looking a little bit more like triangles—not being parabolic, but getting more comfortable—at the expense of adding latency to the gameplay.

And of course, **latency is something that I crusade against** in almost all other cases. It's strange for me to be saying, *"Well, we're gonna add latency here, we're gonna spend latency to try to make it more comfortable."*

This was having some good benefits. It was something—it's hard to test, it's hard to evaluate. Like, *"How much less uncomfortable are you getting from this?"* You have the tests that run up and down the mountains over and over and say, *"Well, do I feel more or less sick?"* It's hard to get back to a baseline and going through the different cases there. But I would go and play for an hour at a time and say, *"This feels better than what it was before."* But I wish there was a more scientific way to make an exact statement about it.

Some other people were complaining about the addition of latency. My thought was that we'd make this a slider where we'd say—and you have to be careful how you word things like this because you don't want it to be something like, *"More comfortable,"* because why would anybody not want to be comfortable? You have to make it the trade-off between **responsiveness and comfort**. And I thought we could have a slider that goes from like one to four—one is just as it is normally and four would be the more linearized that you could, about the most that you could tolerate before really hating the latency—and we leave it up to users.

But after beating on the problem a little bit more and trying some of these tricks about like identifying exactly when you just start to jump so I could start the linearization there, I started looking more closely at the actual data of what all these transitions were. And it should have been obvious again at the beginning, but there's a 20 Hertz tick and **everything is deterministic**. A jump always has the same set of changes—I think it went up to 99 frames to go all the way to the top and land on the next block up, or 12 if you wind up coming all the way down to the ground.

So there were basically three important cases that happened here: there was **jumping up landing on the next block**, there was **jumping up and landing on the same level**, and then there was **walking off and falling down** to the level below. And it turned out that there are a small table of like 20 values that I would take from position and velocity offsets. So I could tell—what I want when you jump from here up to there is not this parabolic arc. I wanted this perfect linear arc that just takes your linear line that just takes you directly up there, and then from here one that just takes you straight down.

Now, these were twelve ticks—this is far more than I would ever try to put in with a lag-and-linearize approach. That would be far too much lag to be comfortably playable. But if I could just make this transition from saying, *"Alright, I know that if you are at this offset from a tile, then you were at the beginning of a jump,"* and I could **map all of these to points along the linearized line**—and this works magically.

This is one of those amazing, this is one of the ideas that really turns out right. And it's clearly that this came from—this was three steps along the way where initial ideas and struggles, working through, then the different things, and then winding up here with something where now you're running around and even if you've got auto-jump on, you bump into the next block and it slides you straight up like it's on a ramp, you go over there and you slide down. And this has been spectacular.

I'm still arguing about whether I need to keep the lag-and-linearize. There's still all these other things—there's the slow starts and the friction stops. This kills dead the problem of single-block step-ups and step-downs, and it works really great. But there are still enough other things where the lag-and-linearize may still wind up having some utility as well.

## The Snake-Walking Problem

There's another aspect of comfort with especially Gear VR in navigation games. The problem is that we only sense where your head mount is—the tracker that we've got is on the headset. So we know where you're looking. We have to assume that you want to move in the direction that you're looking. So when you're going forward, you're going in the direction of the head.

Now that causes a **"snake walking"** where if you're looking around while you're walking, instead of walking straight and looking around—kind of like you want on a linear path that would be comfortable—you're weaving as you go through it. And that's not comfortable. The more you look around with your head, the more that happens.

So lag-and-linearize helps that a little bit where instead of taking a weaving path, you wind up taking more of a linearized path. But it's still probably not really what you want.

So the other thing that's being at least experimented with as a direction there is that maybe we need to have **some offsets between allowing you to look around for some amount of time before changing your actual direction of body movement**. Now what I'd really like—I argue for this on a regular basis—if we had a controller that also had the IMU inside it so that we could at least track yaw between it, then you could clearly say, *"Well, the controller determines what direction you're going. When you turn in your swivel chair, the controller changes your body direction, your turn direction, and you could turn your head completely independently from that."*

Maybe we get that at some point. I don't think it's in the cards right now. So hacking something around for anti-snake-walking, maybe as an aspect of lag-and-linearize, maybe something different.

But this was all—and this is all again mostly stuff that's happened in the last month or two—different ideas that come on. They track kind of continuously about all the different things that are going on.

## Racing Against Time

There's stuff that I'd love to get back to with some of the vision research work for inside-out tracking, where there's that hazard again: if I get something that I think is a good idea and I don't get to beat on it soon enough, it starts perhaps solidifying into a pet idea in some way where maybe I won't be as harsh on it when I do finally get around to working on it. So I worry about that. I just wish again that there was more time to be doing all the different things that I want to be investigating.

And there's even things that, when I go even further afield and start thinking about fusion energy or other things like that, I get ideas for that that I'd like to be trying but probably are not going to be happening in the real near future.

## The Takeaway

But the big takeaway that I want to leave about this is: by looking at the ideas, it's about **taking the joy in the having of the idea and cultivating that**—making that one of the things that you really look for. But **challenging them and not feeling at all bad when they get knocked down**, because usually the process winds up leading to at least a better insight about things, or a better way of looking at things, or techniques that lead to better techniques that solve the problems even better.

---

*[Applause]*

Do we have any time for any questions or anything?
