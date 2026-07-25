# Safety of Live System Use

This chapter explains, step by step, how to reason about the safety of the system as it is actually used today. The key idea is that a repository can contain many technical ideas, but only a narrow part of the system is live, and safety must be judged at that live boundary rather than at the level of all code on disk.

## 1. What this chapter covers

This chapter is about live system use, not theoretical capability and not dormant code that happens to exist in the repository. It asks a practical question: what is actually running, what is only present as files, and what does that difference mean for safety?

For rural developers, that distinction matters because small teams often carry old experiments, archived services, and half-finished ideas alongside the real production path. If those are not separated clearly, it becomes easy to mistake “present in the repo” for “active in the system.”

## 2. What was checked

The review focused on candidate autonomous action services and asked whether they were part of the active deployment path. The result was that those candidate services were not running, and the live deployment path did not reference them.

That matters because it changes the security question from “How do we stop a live autonomous action surface?” to “How do we keep dormant code dormant and keep the live system narrow?” The first question suggests an emergency retrofit; the second suggests disciplined deployment practice.

## 3. What is live

The live system is the part that handles ordinary civic questions and the guarded belief or promotion boundary. In other words, the active path is narrow, controlled, and limited to the actions that are actually needed today.

This is the important safety result. The running system is not the same thing as the whole repository, and the active safety boundary is much smaller than the collection of files on disk might suggest.

## 4. What is not live

The candidate autonomous dispatchers were not running as deployed infrastructure. They were present as code artifacts, but they were not part of the startup path used by the live system.

For a rural developer, this is a common and useful distinction. A dormant service may still matter later, but it does not create the same immediate risk as a service that is actually running and taking actions today.

## 5. Why this matters for safety

Safety depends on where action is actually possible. If a service is dormant, the immediate risk is low; if it is live, the controls must be much stronger.

This chapter therefore treats “live use” as the main safety boundary. That keeps the discussion honest and prevents overreacting to code that is not currently deployed. It also keeps the thesis aligned with the actual system rather than with assumptions about what the system might someday do.

## 6. The current control boundary

The live system already routes its meaningful actions through a guarded boundary. That means the place where the system can actually act is also the place where review, approval, or denial is supposed to happen.

This is the correct pattern for a small or rural team because it reduces the number of places where a mistake can become a live incident. Instead of trying to secure every idea or file equally, the system concentrates safety at the point where action becomes real.

## 7. The deployment rule

If any dormant autonomous service is ever brought into production, it should not be allowed to act by default. It should first be routed through a fail-closed review path, tested against known-good and known-bad cases, and only then permitted to run.

That is a deployment rule, not a retroactive cleanup rule. The current system does not need to be rebuilt around a hypothetical live risk; it needs to keep its live boundary narrow and apply the same discipline when future services are turned on.

## 8. What this chapter does not claim

This chapter does not claim the repository is harmless. It says only that the specific autonomous action surface discussed in the audit is not deployed today.

It also does not claim that all future deployments will be safe automatically. Instead, it argues that future autonomous components must be treated as new live surfaces and gated accordingly.

## 9. What rural developers should take from this

The practical lesson is to separate three things clearly: files on disk, services that are deployed, and actions that are actually possible. That separation prevents confusion and helps a small team focus limited attention on the real safety boundary.

In a rural development setting, that discipline is especially valuable because the team may not have many operators, many reviewers, or many opportunities to recover from a mistaken deployment. Clear live-system boundaries make the work safer and easier to explain.

## 10. Conclusion

The live system is safe in its current use because the risky autonomous services are dormant and not part of the deployed path. The running system’s actions are narrow, controlled, and already subject to a guarded boundary.

The correct safety response is not to treat dormant code as an immediate threat. It is to keep the live boundary fail-closed and require the same discipline any time a dormant autonomous component is brought into production.
