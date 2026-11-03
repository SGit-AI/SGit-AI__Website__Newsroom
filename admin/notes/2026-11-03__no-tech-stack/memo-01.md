# Memo: no tech stack to maintain (3 November 2026)

Dinis Cruz, voice memo to the newsroom writer, transcribed and lightly cleaned. Names of tools as spoken
("Eskit" is sgit).

Also in this message: update the padel sleeve shop vault to say a shop should not be run on GitHub Pages
or as a vault. Done the same day.

---

I would like to write an article about the power of the design simplicity, the design elegance, of no
backend, no real backend, when you have our kind of sgit plus PKI solution. There is an engineering
simplicity, an engineering elegance, but also capability, and less moving parts, in having an application
that does not have a real backend database and all that jazz. sgit makes that possible, because what sgit
gives you is an encrypted data store.

So yes, you have a little bit of a backend, but you have a couple of modules, all on the commodity scale,
each doing a couple of little things. You still need a place to host your web pages, and a place to put
your encrypted files, and in a lot of cases that's it. You might need a way to do authentication, or an
LLM provider, or a couple of other services. Apart from those big commodity services, you bring no tech
stack of your own. Maybe that's the way to say it: it's not that there's no backend; it's that there is no
tech stack you have to maintain apart from an HTML application: the JavaScript, the HTML and the CSS.

And we still have access to all the primitives you usually need:

- Data files, hosted on fast cloud storage, and with sgit on an immutable data store, so they can be
  cached for a long time.
- If you need a database, to run queries that are better done in a database, you run a database on the
  client. We have already explored enough of them: load the data, put it in the client database, show it
  in the browser. That works quite effectively.
- With passkeys you can authenticate users with a browser or device passkey, so you can have a whole user
  experience without having server-side data to protect, and without the complexity in the backend to
  process it. That forces you to design good, elegant solutions, which are not that complicated on the
  client side.
- Events flying back and forward with the append lanes of vaults: send messages to a user, from the
  backend, stored in the vault on the server.
- LLMs in the mix, running in the browser, or mainly in the browser.
- If you need an agentic workflow, depending on scale, run it on one of the main cloud providers: a loop
  that runs, which also gives you maximum provenance, and leverages the intelligence of those platforms.
- My logic is that you use LLMs so as not to use LLMs: the most deterministic you can be, and if you need
  something, you do it on the client side.

What is still missing, temporarily, because the industry hasn't fully caught on: a nice way to give keys,
for example, to the client. Apart from that, it's all pretty good.

And with vaults as distribution, I can host this on a particular domain, over static pages, GitHub Pages
or any other static host, and use the vaults to store apps, to maintain them, or to store the data they
need. And PKI for the users: to store data, and to encrypt data between users. How powerful is that?
