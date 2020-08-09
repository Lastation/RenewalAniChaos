import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         f.SquareShape(cp, 1, "Target", 50, 0);
         f.SquareShape(cp, 1, "Target", 100, 0);

         KillUnitAt(All, "Target", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.count[cp] += 1;
      }
      else if (f.count[cp] == 1)
      {
         f.SquareShape(cp, 1, "60 + 1n Danimoth", 150, 0);
         f.SquareShape(cp, 1, "60 + 1n Danimoth", 100, 50);
         f.SquareShape(cp, 1, "60 + 1n Danimoth", 50, 100);
         f.SquareShape(cp, 1, "40 + 1n Marine", 100, 50);
         f.SquareShape(cp, 1, "40 + 1n Marine", 50, 100);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.count[cp] += 1;
      }
      else if (f.count[cp] == 2)
      {
         f.SquareShape(cp, 1, "60 + 1n Archon", 150, 0);
         f.SquareShape(cp, 1, "60 + 1n Archon", 100, 50);
         f.SquareShape(cp, 1, "60 + 1n Archon", 50, 100);

         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

         f.SkillWait(cp, 240);
         
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);
         f.distance[cp] = 50;

         f.SquareShape(cp, 1, "60 + 1n Archon", 100, 0);

         f.DotShape(cp, 1, "40 + 1n Goliath", f.distance[cp], f.distance[cp]);
         f.DotShape(cp, 1, "40 + 1n Goliath", -f.distance[cp], -f.distance[cp]);
         f.DotShape(cp, 1, "Kakaru (Twilight)", f.distance[cp], f.distance[cp]);
         f.DotShape(cp, 1, "Kakaru (Twilight)", -f.distance[cp], -f.distance[cp]);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

         f.SkillWait(cp, 160);
         
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

         f.SquareShape(cp, 1, "60 + 1n Archon", 75, 75);

         f.DotShape(cp, 1, "40 + 1n Goliath", 0, 50);
         f.DotShape(cp, 1, "40 + 1n Goliath", 0, -50);
         f.DotShape(cp, 1, "Kakaru (Twilight)", 0, 50);
         f.DotShape(cp, 1, "Kakaru (Twilight)", 0, -50);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

         f.SkillWait(cp, 160);
         
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 5)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

         f.SquareShape(cp, 1, "60 + 1n Archon", 100, 0);

         f.DotShape(cp, 1, "40 + 1n Goliath", -50, 50);
         f.DotShape(cp, 1, "40 + 1n Goliath", 50, -50);
         f.DotShape(cp, 1, "Kakaru (Twilight)", -50, 50);
         f.DotShape(cp, 1, "Kakaru (Twilight)", 50, -50);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

         f.SkillWait(cp, 160);
         
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 6)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

         f.SquareShape(cp, 1, "60 + 1n Archon", 75, 75);

         f.DotShape(cp, 1, "40 + 1n Goliath", -50, 0);
         f.DotShape(cp, 1, "40 + 1n Goliath", 50, 0);
         f.DotShape(cp, 1, "Kakaru (Twilight)", -50, 0);
         f.DotShape(cp, 1, "Kakaru (Twilight)", 50, 0);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

         f.SkillWait(cp, 160);
         
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 7)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }
}