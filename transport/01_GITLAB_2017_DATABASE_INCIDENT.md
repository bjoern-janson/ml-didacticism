# AG/1 Transport Test 01 — GitLab January 31, 2017 Database Incident

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Test status:** COMPLETED  
**External-domain class:** software operations / database incident / debugging and recovery

---

# 1. Corpus boundary

This run uses one bounded external source only:

```text
Title: Postmortem of database outage of January 31
Publisher: GitLab
Published: February 10, 2017
URL: https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/
```

Included:

```text
database setup
timeline
broken recovery procedures
recovery plan and execution
data-loss impact
root-cause analysis
```

Excluded as evidence for this run:

```text
linked GitLab issues
public live incident document
Twitter status posts except as quoted/described by the bounded postmortem
YouTube stream
later GitLab articles
outside technical documentation
```

The source is retrospective. Therefore all source-level historical assertions remain provenance-bound to the postmortem rather than being treated as direct unmediated access to reality.

---

# 2. Architecture available during the run

Only:

```math
\boxed{
RELATION
+
REPRESENTATION
+
SOURCE\_PROVENANCE
+
OPEN
}
```

No primitive:

```text
ENTITY
STATE
EVENT
TIME
ACCESS
COMMITMENT
AUTHORITY
```

is available.

Readable labels such as `db1`, `db2`, `engineer`, `snapshot_6h`, and `GitLab.com` are display aliases for derived referential classes over local argument occurrences. They are **not** stored primitive entity IDs.

---

# 3. Source-native incident grammar

A source-constrained compression is:

```math
\boxed{
\text{fresh production snapshot}
\rightarrow
\text{database load increase}
\rightarrow
\text{initial spam suspicion}
\rightarrow
\text{later expanded load account}
\rightarrow
\text{secondary replication lag/failure}
\rightarrow
\text{manual secondary rebuild attempt}
\rightarrow
\text{pg\_basebackup wait / low observability}
\rightarrow
\text{engineer hypothesis about secondary data directory}
\rightarrow
\text{host misidentification}
\rightarrow
\text{primary data removal}
\rightarrow
\text{backup search}
\rightarrow
\text{recovery mechanisms found unavailable/broken}
\rightarrow
\text{six-hour snapshot selected}
\rightarrow
\text{slow restoration}
\rightarrow
\text{service restoration with known data loss}
\rightarrow
\text{later root-cause decomposition}
}
```

The architecture must preserve at least these source distinctions:

```math
\boxed{
\text{historical operation}
\neq
\text{operator representation of target host}
}
```

```math
\boxed{
\text{initial causal suspicion}
\neq
\text{later causal account}
}
```

```math
\boxed{
\text{backup procedure intended/configured}
\neq
\text{backup successfully produced}
\neq
\text{team awareness of backup failure}
}
```

```math
\boxed{
\text{recovery plan}
\neq
\text{recovery execution}
\neq
\text{restored service}
}
```

```math
\boxed{
\text{restored database}
\neq
\text{recovered all lost data}
}
```

---

# 4. Historical relation reconstruction

The following is representative rather than exhaustive. Relation-instance labels (`h1`, `h2`, ...) are addressable relation occurrences, which are permitted by the frozen `RELATION` kernel.

## Database topology

```text
h1 = HAS_ROLE(db1, primary_database)
h2 = HAS_ROLE(db2, secondary_database)
h3 = HOT_STANDBY_FOR(db2, db1)
h4 = USED_FOR(db2, failover)
```

Source provenance: postmortem database-setup section.

No primitive `ENTITY` is needed: `db1` and `db2` are derived referent views over their source-grounded argument occurrences.

## Fresh staging snapshot

```text
h5 = TAKES_SNAPSHOT(engineer, production_database, snapshot_6h)
h6 = LOADS_INTO(snapshot_6h, staging_environment)
h7 = APPROX_CLOCK_INDEX(h5, 2017-01-31T17:20Z)
```

`APPROX_CLOCK_INDEX` is an explicit relation, not a hidden timestamp field.

## Load increase and first operational account

```text
h8 = DATABASE_LOAD_INCREASES(GitLab.com)
h9 = USERS_UNABLE_TO_POST_COMMENTS(many_users)
h10 = BEFORE(h8, replication_failure)
```

The source initially frames spam as suspected cause. That suspicion is not inserted as historical truth; it is represented separately below.

## Replication failure

```text
h11 = REPLICATION_LAGS(db2)
h12 = REPLICATION_FAILS(db2)
h13 = WAL_SEGMENTS_REMOVED_BEFORE_REPLICATION(db1, db2)
h14 = REQUIRES_MANUAL_RESYNCHRONIZATION(db2)
h15 = REBUILD_PROCEDURE_REQUIRES_EMPTY_DATA_DIRECTORY(db2)
```

## Secondary rebuild attempt

```text
h16 = WIPES_DATA_DIRECTORY(engineer, db2)
h17 = RUNS(engineer, pg_basebackup, db2)
h18 = WAITS_WITHOUT_MEANINGFUL_OUTPUT(pg_basebackup)
h19 = REPORTS_CONNECTION_LIMIT(pg_basebackup, max_wal_senders)
h20 = CHANGES_SETTING(engineers, max_wal_senders, 3, 32)
h21 = POSTGRESQL_RESTART_REFUSED(postgresql)
h22 = CHANGES_SETTING(engineers, max_connections, 8000, 2000)
h23 = POSTGRESQL_RESTARTS(postgresql)
h24 = RUNS_WITH(engineer, pg_basebackup, strace)
h25 = SHOWS(strace, poll_wait)
```

These are typed relations/occurrences. No `EVENT` object is necessary.

## Destructive host mistake

The source then gives the critical historical occurrence:

```text
h26 = WIPES_DATA_DIRECTORY(engineer, db1)
h27 = HAS_ROLE(db1, primary_database)
h28 = TERMINATES(engineer, h26)
h29 = AFTER(h28, h26_started)
h30 = DATA_REMOVED_FROM(db1, approximately_300GB)
```

The operator's incorrect target representation is kept in a separate representation scope below.

## Backup search and failure

```text
h31 = SEARCHES_FOR(engineers, database_backups)
h32 = S3_BUCKET_CONTENT(s3_backup_bucket, empty)
h33 = NO_RECENT_BACKUP_FOUND(engineers)
h34 = USES_VERSION(pg_dump_procedure, PostgreSQL_9_2)
h35 = DATABASE_VERSION(production_database, PostgreSQL_9_6)
h36 = VERSION_MISMATCH_CAUSES_FAILURE(pg_dump_procedure)
h37 = CRON_FAILURE_NOTIFICATION_SENT_BY(email)
h38 = EMAIL_NOT_DMARC_SIGNED(cron_notification)
h39 = RECEIVER_REJECTS(cron_notification)
h40 = NOT_AWARE_OF(team, pg_dump_backup_failure)
```

`NOT_AWARE_OF` is a source-earned informational relation. No universal `ACCESS` bit is introduced.

## Snapshot availability

```text
h41 = SNAPSHOT_AGE(snapshot_daily, approximately_24_hours)
h42 = SNAPSHOT_AGE(snapshot_6h, approximately_6_hours)
h43 = AVAILABLE_FOR_RECOVERY(snapshot_6h)
h44 = NOT_ENABLED_FOR(database_servers, azure_disk_snapshots)
```

## Recovery

```text
h45 = SELECTS_FOR_RECOVERY(engineers, snapshot_6h)
h46 = MOTIVE_REPRESENTED_AS(h45, minimize_data_loss)
h47 = COPIES(staging_database, production_host)
h48 = COPY_DURATION(h47, approximately_18_hours)
h49 = BOTTLENECK(staging_disks, restoration_copy)
h50 = RESTORES_DATABASE_TO(production_database, 2017-01-31T17:20Z_content)
h51 = RESTORES_WITHOUT(production_database, webhooks)
h52 = LATER_RESTORES(production_database, webhooks)
h53 = CONFIRMS_OPERATING_AS_EXPECTED(team, GitLab.com)
```

The time/index values occur as explicit relation arguments, not hidden temporal coordinates.

## Data-loss boundary

```text
h54 = DATABASE_CHANGES_LOST(window_17_20_to_23_30)
h55 = GIT_REPOSITORIES_NOT_REMOVED(git_repositories)
h56 = WIKIS_NOT_REMOVED(wikis)
h57 = AFFECTED_ESTIMATE(projects, at_least_5000)
h58 = AFFECTED_ESTIMATE(comments, at_least_5000)
h59 = AFFECTED_ESTIMATE(users, roughly_700)
```

Thus:

```math
\boxed{
\text{service restored}
\neq
\text{all prior database modifications recovered}
}
```

No `STATE` primitive is needed to preserve that distinction.

---

# 5. Representation scopes

This incident strongly tests the frozen assertion-scope boundary.

## R1 — initial load hypothesis

The source says the increased load was initially suspected to be spam-related, and later reports that a background employee-removal job also contributed.

Represent:

```text
rho_load_initial
    source = GitLab operators / postmortem report of their then-current suspicion
    mode = suspicion
    content:
        CAUSES(spam, database_load_increase)
```

Historical/source-later assertions separately include:

```text
BACKGROUND_JOB_REMOVES(employee_account_data)
CONTRIBUTES_TO(background_job, database_load_increase)
```

Therefore:

```math
\boxed{
content(\rho_{load\_initial})
\neq
\text{later retrospective causal graph}
}
```

No contradiction occurs.

## R2 — engineer's `pg_basebackup` hypothesis

At approximately 23:30 UTC, the engineer thought prior `pg_basebackup` attempts might have created files in the secondary data directory.

```text
rho_pgdata
    holder = engineer
    mode = hypothesis
    content:
        FILES_PRESENT_IN_DATA_DIRECTORY(db2)
        BLOCKS_OR_EXPLAINS_WAIT(pg_basebackup, files_present)
```

The postmortem later reports a different explanation: another engineer said the silent wait was normal while waiting for the primary to send replication data.

That later explanation is preserved separately rather than rewriting `rho_pgdata`.

## R3 — decisive wrong-host representation

Historical assertion:

```text
WIPES_DATA_DIRECTORY(engineer, db1)
HAS_ROLE(db1, primary_database)
```

Operator representation at action time:

```text
rho_host
    holder = engineer
    mode = operational target representation
    content:
        CURRENT_TARGET(db2)
        HAS_ROLE(db2, secondary_database)
```

The source explicitly says the engineer errantly thought the operation was being performed on the secondary while it was actually executed on the primary.

Thus:

```math
\boxed{
\mathcal H:\ target=db1
\qquad
\neq
\qquad
content(\rho_{host}):\ target=db2
}
```

This is a direct non-Genesis transport of the frozen representation distinction.

The false model is also causally active: it participates in why the destructive operation is initiated against the wrong referent.

## R4 — backup sufficiency assumption

The source later explains that Azure disk snapshots were not enabled on database servers because the team assumed the other backup procedures were sufficient.

```text
rho_backup_sufficiency
    holder/source = GitLab operational organization as reported retrospectively
    mode = prior assumption
    content:
        SUFFICIENT(other_backup_procedures, disaster_recovery)
```

Historical/source-later assertions include:

```text
PG_DUMP_BACKUPS_NOT_WORKING
REPLICATION_UNAVAILABLE_FOR_RECOVERY
AZURE_DB_SNAPSHOTS_NOT_ENABLED
```

The architecture cleanly preserves:

```math
\boxed{
\text{prior represented sufficiency}
\neq
\text{later observed recovery capability}
}
```

## R5 — uncertain webhook recovery content

The recovery plan says the snapshot might still contain webhooks and explicitly notes uncertainty.

```text
rho_webhooks
    source = recovery team / postmortem
    mode = uncertain recovery hypothesis
    content:
        CONTAINS(snapshot_copy, webhooks)
```

The exact relation is not promoted to history at plan time.

An `OPEN` bridge records the uncertainty until later recovery operations resolve enough of the issue for the source's purposes.

## R6 — later root-cause analysis

The postmortem's 5-Whys section is a later structured explanation of the earlier incident.

It must not erase the earlier timeline or initial hypotheses.

Represent:

```text
rho_rca
    source = GitLab postmortem
    mode = retrospective causal analysis
    content:
        CAUSED_BY(service_outage, primary_database_directory_removal)
        CAUSED_BY(primary_database_directory_removal, manual_replication_recovery_path + wrong_host_operation)
        CAUSED_BY(replication_failure, increased_database_load + missing_WAL_segments)
        ...
```

The exact causal claims remain provenance-tagged as the postmortem's retrospective analysis.

Therefore:

```math
\boxed{
\text{timeline assertions}
\neq
\text{initial operator hypotheses}
\neq
\text{later root-cause representation}
}
```

---

# 6. Referential reconstruction without ENTITY

The case contains repeated references to:

```text
primary database
db1.cluster.gitlab.com
production database
primary host
```

and separately:

```text
secondary database
db2.cluster.gitlab.com
secondary host
standby
```

Persistent reference is reconstructed through source-supported coreference relations over local argument occurrences:

```text
SAME_REFERENT(o_db1_hostname, o_primary_database)
SAME_REFERENT(o_db1_primary, o_actual_wipe_target)

SAME_REFERENT(o_db2_hostname, o_secondary_database)
SAME_REFERENT(o_db2_secondary, o_intended_rebuild_target)
```

No canonical entity key is required.

The crucial wrong-host case depends precisely on **not** collapsing `db1` and `db2` while still linking their repeated mentions correctly.

---

# 7. Temporal reconstruction without TIME

The source contains explicit approximate times and durations.

Represent them as relation facts:

```text
APPROX_CLOCK_INDEX(h5, 17:20_UTC)
APPROX_CLOCK_INDEX(h8, 19:00_UTC)
APPROX_CLOCK_INDEX(h11, 23:00_UTC)
APPROX_CLOCK_INDEX(h26, 23:30_UTC)
BEFORE(h8,h11)
BEFORE(h11,h26)
COPY_DURATION(h47, approximately_18_hours)
```

The architecture preserves both:

```math
\boxed{
\text{temporal order}
\neq
\text{temporal metric}
}
```

without a hidden clock carrier.

---

# 8. Failed and successful operations without EVENT/STATE

The source requires all of these to remain distinct:

```text
pg_basebackup runs but waits
PostgreSQL restart fails
configuration is changed
PostgreSQL restart later succeeds
strace runs but yields little explanatory information
data-directory removal starts
operator terminates removal
backup search occurs but recent backup is not found
recovery copy proceeds slowly
service is eventually confirmed operating
```

All reconstruct as addressable relation occurrences plus ordering relations.

No separate event or state carrier is required.

---

# 9. Provenance stress test

The incident contains several provenance levels:

```text
postmortem source-level historical assertion
operator's then-current hypothesis
another engineer's later explanation
team's prior assumption about backup sufficiency
recovery plan under uncertainty
postmortem's later 5-Whys causal account
```

AG/1 can preserve these without conflation because:

```text
RELATION carries source-earned typed assertions
REPRESENTATION carries scoped content
SOURCE_PROVENANCE records which source/mode supplied each assertion
OPEN prevents unearned bridges
```

A particularly strong example is:

```math
\boxed{
\text{engineer thinks target is secondary}
\neq
\text{operation actually targets primary}
}
```

and another is:

```math
\boxed{
\text{team assumed backup procedures sufficient}
\neq
\text{backup procedures available at recovery time}
}
```

---

# 10. Hidden-parameter audit

Search the reconstruction for deleted primitives.

## ENTITY

No global canonical participant ID is necessary. Readable aliases are derived views; source-grounded coreference links connect argument occurrences.

**Audit:** PASS.

## STATE

No world-state object is stored. Relations such as `REPLICATION_FAILS`, `S3_BUCKET_CONTENT(...,empty)`, and `OPERATING_AS_EXPECTED` are independently typed assertions.

**Audit:** PASS.

## EVENT

Operations/failures are addressable relation instances, not event records with hidden participant fields.

**Audit:** PASS.

## TIME

Times and durations are explicit relations; no timestamp field is attached to every relation.

**Audit:** PASS.

## ACCESS

Informational distinctions use source predicates such as `NOT_AWARE_OF`, `REPORTS`, `SHOWS`, and representation scopes. No access bit exists.

**Audit:** PASS.

## COMMITMENT / AUTHORITY

The bounded incident does not require either as a primitive. Operational commands/plans/decisions, where present, remain local typed predicates.

**Audit:** PASS.

## Representation tax evasion

No arbitrary `context=` field replaces `REPRESENTATION`. False/uncertain/hypothetical/retrospective content is explicitly scoped through the frozen representation kernel.

**Audit:** PASS.

---

# 11. Smallest potential failure witnesses considered

## Candidate F1 — mistaken target identity

Could AG/1 distinguish:

```text
actual target = primary
operator model target = secondary
```

without an ENTITY or STATE primitive?

Yes.

Referential classes reconstruct primary and secondary independently, while `rho_host` contains the false target relation under non-history scope.

**No failure.**

## Candidate F2 — backup failed without team awareness

Could AG/1 distinguish:

```text
backup procedure fails
notification email exists
notification rejected
team unaware
```

without ACCESS?

Yes, through explicit relation chain plus `NOT_AWARE_OF`.

**No failure.**

## Candidate F3 — initial suspicion versus later causal analysis

Could AG/1 preserve both without making history contradictory?

Yes. The initial suspicion and later 5-Whys account occupy different provenance-bearing representation scopes.

**No failure.**

## Candidate F4 — operation with unsuccessful/partial consequence

Could AG/1 represent a process that starts, is terminated, but has already removed substantial data?

Yes. Separate relation occurrences preserve start/removal/termination and their ordering.

**No failure.**

## Candidate F5 — recovery restores service but not all data

Could AG/1 represent service restoration and irreversible data loss simultaneously without STATE?

Yes. They are independent historical relations.

**No failure.**

---

# 12. Verdict

```text
PASS
```

More precisely:

```math
\boxed{
\textbf{AG/1 reconstructs the bounded GitLab January 31, 2017 database-incident postmortem without introducing a new architecture primitive.}
}
```

The strongest transport witness is the wrong-host operation:

```math
\boxed{
\text{historical target relation}
\neq
\text{operator's represented target relation}
}
```

and the architecture preserves that difference using exactly the frozen world/history-versus-representation split.

The incident also transports:

```text
initial hypothesis ≠ later causal account
configured recovery procedure ≠ functioning recovery procedure
failure occurrence ≠ team awareness of failure
recovery plan ≠ recovery execution
service restoration ≠ complete data recovery
```

without reopening `STATE`, `EVENT`, `TIME`, `ACCESS`, `ENTITY`, `COMMITMENT`, or `AUTHORITY`.

---

# 13. Claim ceiling

This PASS does **not** establish domain-generality.

It establishes one bounded result only:

```math
\boxed{
\textbf{the first independent software-incident corpus tested did not force a distinction outside frozen AG/1.}
}
```

The architecture remains frozen.

A later failing corpus must be recorded as failure evidence rather than repaired in place.

---

# Transport compression

```math
\boxed{
\text{GitLab incident history}
=
\text{typed provenance-bearing relations}
+
\text{scoped operator/team/postmortem representations}
}
```

No new primitive was earned by this test.
