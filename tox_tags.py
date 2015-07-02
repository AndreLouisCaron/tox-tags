# -*- coding: utf-8 -*-

import os
import tox

@tox.hookimpl
def tox_addoption(parser):
    # Grab `tags` config from [testenv] sections.
    parser.add_testenv_attribute(
        name='tags',
        type='line-list',
        help='',
        default=[],
    )
    # Grab `-t` and `--tagged` command-line options.
    parser.add_argument(
        '-t, --tagged',
        action='append', dest='tags',
        default=[],
        type=str,
    )


@tox.hookimpl
def tox_configure(config):
    tags = config.option.tags
    if not tags and 'TOX_TAGS' in os.environ:
        tags = os.environ['TOX_TAGS'].split(':')
    if tags:
        rules = map(_make_rule, tags)
        # Note: keep envlist in original order!
        config.envlist = [
            envname for envname in config.envlist
            if _select(rules, config.envconfigs[envname].tags)
        ]


def _split(t):
    if '=' in t:
        return t.split('=', 1)
    return (t, 1)


def _select(rules, tags):
    tags = dict(map(_split, tags))
    return any(r(tags) for r in rules)


def _make_rule(rule):
    rule = map(_compile, rule.split(','))
    def _match_rule(tags):
        return all(subrule(tags) for subrule in rule)
    return _match_rule


def _compile(expr):
    if expr.startswith('!'):
        return lambda tags: expr[1:] not in tags
    if '=' in expr:
        k, v = expr.split('=', 1)
        return lambda tags: tags.get(k) == v
    return lambda tags: expr in tags
