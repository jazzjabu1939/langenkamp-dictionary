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
  --date YYYY-MM-DD \
  --summary-zh "本期的主題是……"
```

Every issue carries a Chinese summary for Chinese readers (added November 14, 2026). Write two or three sentences in Traditional Chinese from the approved issue: what the issue is mainly about, then its other main items. Check every number, name and claim against the issue before publishing; keep institution names in English and translate ordinary terms. The command refuses to publish without `--summary-zh`, and `status` fails if any published issue lacks one.

The summary is stored as `summary_zh` in the issue's front matter and shown by `_includes/zh-summary.html`: a click-to-open block under the header that opens by itself when the reader's browser language is Chinese. The summary appears only on langenkamp.io, not in the emailed brief or the PDF.

Publication is guarded. The command:

1. Requires the volume to equal the ledger's next volume.
2. Confirms the source header and date.
3. Refuses duplicate dates and existing site files.
4. Creates the public Jekyll issue page, with the Chinese summary block under the header.
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
