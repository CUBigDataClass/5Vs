

val prefix = "fs.swift.service.<name>"

val hconf = sc.hadoopConfiguration

hconf.set(prefix + ".auth.url", "<auth_url>/v2.0/tokens")

hconf.set(prefix + ".auth.endpoint.prefix", "endpoints")

hconf.set(prefix + ".tenant", "<project_id>")

hconf.set(prefix + ".username", "<user_id>")

hconf.set(prefix + ".password", "<password>")

hconf.setInt(prefix + ".http.port", 8080)

hconf.set(prefix + ".region", "<region>")

hconf.setBoolean(prefix + ".public", true)