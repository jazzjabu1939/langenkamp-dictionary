# Newsletter Publication Workflow

`newsletter/ledger.json` is the definitive volume record for the **AI in Higher Education - Weekly Brief**.

Only entries marked `published` advance the numbering. Draft filenames and unpublished site files never determine the next volume.

## Check the next volume

From the `langenkamp-dictionary` repository:

```sh
python3 scripts/newsletter_workflow.py status
```

The command validates unique volumes, unique publication dates, an unbroken published sequence, and the presence of every published site file.

## Start a correctly numbered draft

```sh
python3 scripts/newsletter_workflow.py new --date YYYY-MM-DD
```

This creates the canonical Markdown draft in `../dept-memos/` and refuses to overwrite an existing file.

## Publish an approved issue

```sh
python3 scripts/newsletter_workflow.py publish \
  --source ../dept-memos/YYYY-MM-DD-education-ai-brief.md \
  --date YYYY-MM-DD
```

Publication is guarded. The command:

1. Requires the volume to equal the ledger's next volume.
2. Confirms the source header and date.
3. Refuses duplicate dates and existing site files.
4. Creates the public Jekyll issue page.
5. Adds the published issue to the ledger.
6. Regenerates the full newsletter archive and the current-issues list in Other Writing.
7. Builds the site.
8. Reports the next volume.

Professor Langenkamp remains the only person who sends the newsletter to colleagues or a department list. Site publication does not authorize external email distribution.

## Repair archive listings

If a listing is edited or becomes stale:

```sh
python3 scripts/newsletter_workflow.py sync
bin/jekyll-local build
```

The ledger, rather than either archive page, remains authoritative.
