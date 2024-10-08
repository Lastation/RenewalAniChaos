import Function as f;

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y);
function NxNSquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, n, interval, x, y);
function EdgeShapeAtWithProperty(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y, property);

function main(cp)
{
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

         if (f.loop[cp] % 2 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            var i = f.loop[cp] / 2;

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 25 + 25 * i, 75 - 25 * i);
            f.SquareShape(cp, 1, "Rhynadon (Badlands)", 25 + 25 * i, 75 - 25 * i);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            f.SquareShape(cp, 1, " Creep. Dunkelheit", 100, 100);
            f.SquareShape(cp, 6, "Bengalaas (Jungle)", 100, 100);
            f.SquareShape(cp, 1, "Target", 100, 100);
            f.DotShape(cp, 1, "Target", 0, 0);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Zealot", 40 + 40 * i, 40 + 40 * i);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
         }
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

         f.SquareShape(cp, 1, "40 + 1n Mutalisk", 120 - 8 * f.loop[cp], 0);
         f.SquareShape(cp, 1, "Protoss Dark Archon", 120 - 8 * f.loop[cp], 0);
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

         f.SquareShape(cp, 1, "40 + 1n Guardian", 170 - 8 * f.loop[cp], 0);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

         if (f.loop[cp] % 2 == 0)
         {
            f.SquareShape(cp, 1, "Scantid (Desert)", 100, 100);
            KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp);
         }

         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 100, 100);
            f.SquareShape(cp, 1, "50 + 1n Tank", 100, 100);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 150, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, 0);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] == 6)
         {
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         }

         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 150, 150);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, 150);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 150);
            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 150);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 75, 75);
            f.SquareShape(cp, 1, "40 + 1n Ghost", 75, 75);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 200, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 200, 0);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 150);
            f.SquareShape(cp, 1, "40 + 1n Ghost", 150, 150);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 6)
         {
            f.SquareShape(cp, 1, "40 + 1n Guardian", 200, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 200, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 19)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            f.EdgeShapeWithProperty(cp, 1, " Unit. Hoffnung 25000", 45, 2, 50, 1);
            f.EdgeShape(cp, 1, "40 + 1n Drone", 0, 2, 30);
            f.NxNSquareShape(cp, 1, " Creep. Licht", 2, 75);
         }
         else if (f.loop[cp] == 2)
         {
            NxNSquareShapeAt(cp, 1, "40 + 1n Guardian", 3, 50, 150, 0);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            EdgeShapeAtWithProperty(cp, 1, " Unit. Hoffnung 25000", 45, 2, 50, 150, 0, 1);
            EdgeShapeAt(cp, 1, "40 + 1n Drone", 0, 2, 30, 150, 0);
            NxNSquareShapeAt(cp, 1, " Creep. Licht", 2, 75, 150, 0);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 150, 0);
         }


         if (f.loop[cp] < 3)
         {
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(All, " Creep. Licht", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(All, "40 + 1n Mutalisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Unit. Hoffnung 25000", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
            Order(" Creep. Licht", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 42)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "40 + 1n Zergling", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, " Creep. Licht", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);

         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

         f.SkillEnd(cp);
      }
   }
}

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y)
{
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, x, y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -x, -y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -y, x);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, y, -x);
}

function EdgeShapeAtWithProperty(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y, property)
{
   f.EdgeShapeAtWithProperty(cp, count, Unit, degree, n, interval, x, y, property);
   f.EdgeShapeAtWithProperty(cp, count, Unit, degree, n, interval, -x, -y, property);
   f.EdgeShapeAtWithProperty(cp, count, Unit, degree, n, interval, -y, x, property);
   f.EdgeShapeAtWithProperty(cp, count, Unit, degree, n, interval, y, -x, property);
}

function NxNSquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, n, interval, x, y)
{
   f.NxNSquareShapeAt(cp, count, Unit, n, interval, x, y);
   f.NxNSquareShapeAt(cp, count, Unit, n, interval, -x, -y);
   f.NxNSquareShapeAt(cp, count, Unit, n, interval, -y, x);
   f.NxNSquareShapeAt(cp, count, Unit, n, interval, y, -x);
}
